import requests
import json
from datetime import datetime

# will allow loading the key I put in the JSON file
with open('key.json') as f:
    config = json.load(f)

# My OpenWeatherMap API Key 
API_KEY = config['API_KEY']

# I tried to make a class to better organize the data
class DailyForecast:
    """Class to store information for a day"""
    
    def __init__(self, date):
        self.date = date
        self.rain = 0  # cumulative rain in mm
        self.snow = 0  # cumulative snow in mm
        self.transitions = 0  # number of weather changes
        self.forecasts_3h = []  # list of forecasts every 3 hours
    
    def add_forecast(self, forecast):
        """Adds a 3-hour forecast to the day"""
        self.forecasts_3h.append(forecast)
    
    def to_dictionary(self):
        """Converts the object to a dictionary for JSON"""
        return {
            'local_date': self.date,
            'rain_cumul_mm': round(self.rain, 1),
            'snow_cumul_mm': round(self.snow, 1),
            'major_transitions_count': self.transitions
        }


def get_forecasts(city, country):
    """
    This function retrieves weather forecasts for a city
    city: the name of the city (string)
    country: 2-letter country code (string)
    """
    # Constructing the URL for the API
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city},{country}&appid={API_KEY}&units=metric"
    
    try:
        # Make the request to the API
        response = requests.get(url) 

        # Check if it worked
        if response.status_code == 200:
            return response.json()
        else:
            print(f"⚠ Error: code {response.status_code}")
            return None
    except Exception as e:
        print(f" ⚠ Problem with the request: {e}")
        return None


def calculate_transitions(day_forecasts):
    """
    Calculates the number of major transitions in a day
    A transition = change in weather AND temperature variation of more than 3°C
    I made a loop, to make it easier
    """
    counter = 0
    
    # Iterate through the forecasts (except the last one because we compare with the next one because we don't have a value after J+5) 
    for i in range(len(day_forecasts) - 1):
        current_forecast = day_forecasts[i]
        next_forecast = day_forecasts[i +1]
        
        # Get the weather category (Clear, Rain, Clouds, etc.)
        current_weather = current_forecast['weather'][0]['main']
        next_weather = next_forecast['weather'][0]['main']
        
        # Get the temperatures
        current_temp = current_forecast['main']['temp']
        next_temp = next_forecast['main']['temp']
        
        # Calculate the temperature difference (absolute value)
        temp_diff = abs(next_temp - current_temp)
        
        # Check if it's a major transition
        if current_weather != next_weather and temp_diff > 3:
            counter += 1  # increment the counter
    
    return counter


def process_weather_data(data):
    """
    Processes the API data and calculates everything needed
    Returns a dictionary with all the information
    """
    # Get the city name and country code
    city_name = data['city']['name']
    country_code = data['city']['country']
    
    # Variables to store totals for the period
    total_rain = 0
    total_snow = 0
    max_humidity = 0
    
    # Dictionary to store DailyForecast objects
    # The key is the date, the value is a DailyForecast object
    days = {}
    
    # Iterate through all forecasts
    for item in data['list']:
        # Extract the date (format: standard)
        date_time = item['dt_txt']
        date = date_time.split(' ')[0]  # Keep only the date
        
        # If it's a new day, create a DailyForecast object
        if date not in days:
            days[date] = DailyForecast(date)
        
        # Add the forecast to the day's object
        days[date].add_forecast(item)
        
        # Calculate the rain 
        if 'rain' in item and '3h' in item['rain']:
            rain_amount = item['rain']['3h']
            days[date].rain += rain_amount  # add to the object
            total_rain += rain_amount
        
                # Calculate the snow 
        if 'snow' in item and '3h' in item['snow']:
            snow_amount = item['snow']['3h']
            days[date].snow += snow_amount  # add to the object
            total_snow += snow_amount
        
        # Check the maximum humidity
        current_humidity = item['main']['humidity']
        if current_humidity > max_humidity:
            max_humidity = current_humidity
    
    # Calculate transitions for each day
    for date, day in days.items():
        num_transitions = calculate_transitions(day.forecasts_3h)
        day.transitions = num_transitions
    
    # Create the list of details (convert objects to dictionaries)
    forecast_details = []
    for date, day in days.items():
        forecast_details.append(day.to_dictionary())
    
    # Create the final result
    result = {
        'forecast_location_name': city_name,
        'country_code': country_code,
        'total_rain_period_mm': round(total_rain, 1),
        'total_snow_period_mm': round(total_snow, 1),
        'max_humidity_period': max_humidity,
        'forecast_details': forecast_details
    }
    
    return result


def save_json(data, filename='result.json'):
    """
    Saves the data to a JSON file
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print(f"File '{filename}' created successfully!")
        return True
    except Exception as e:
        print(f"Error during saving: {e}")
        return False


# Main program
def main():
    print("Hello and Welcome!")
    print("This is my weather forecast program!")
    print()
    
    # Ask the user for the city and country
    city = input("➡ Enter the city name: ")
    country = input(" ➡ Enter the country code (2 letters, e.g. FR, US, GB): ")
    
    # Check that the inputs are not empty
    if not city or not country:
        print(" ⛔ Error: you must enter a city and a country!")
        return
    
    # Check that the country code is 2 characters
    if len(country) != 2:
        print(" ⛔ Error: the country code must be 2 letters!")
        return
    
    print()
    print(f"Retrieving forecasts for {city}, {country.upper()}...")
    
    # Get the data from the API
    data = get_forecasts(city, country)
    
    if data is None:
        print("Unable to retrieve data. Check the city/country.")
        return
    
    print("Data retrieved! Processing in progress...")
    
    # Process the data
    result = process_weather_data(data)
    
    # Display the result of the input of the user
    print()
    print("Forecast summary:")
    print(f"Location: {result['forecast_location_name']}, {result['country_code']}")
    print(f"🌧️ Rainfall total (5 days): {result['total_rain_period_mm']} mm")
    print(f"❄️ Snowfall total (5 days): {result['total_snow_period_mm']} mm")
    print(f"Maximum humidity: {result['max_humidity_period']}%")
    print(f"Number of days analyzed: {len(result['forecast_details'])}")

    # Save to a JSON file
    print()
    save_json(result)


"""Every 3H the API will get the results of the forecast, so it will be doing 5x24h. All days won't be fully counted hence why we got a result at 6 days.
If we want a full 5 days results, we must start the forecast the day before at 21h (+3h = 00h of the following day) at J1."""

# Will launch the bloc main 
if __name__ == "__main__":
    main()
