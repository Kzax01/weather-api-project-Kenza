**Welcome to my OpenWeatherMap Weather Forecast Project**


**Description**
------------


This project uses the OpenWeatherMap API to retrieve 5-day weather forecasts for a specific city and country. It generates a JSON file containing weather information, including accumulated precipitation, the number of major weather transitions, etc.


**Prerequisites**
------------


* Python 3.13.5 or later
* OpenWeatherMap API Key (see the section below)


**Installation**
------------


1.  Create a virtual environment with `python -m venv venv`
2.  Activate the virtual environment with `.\venv\Scripts\activate` (on Windows) or `source venv/bin/activate` (on Linux/Mac)
3.  Install the dependencies with `pip install -r requirements.txt`


This will create a virtual environment containing only the dependencies necessary for the project.


**Usage**
-------------


1.  Create a `key.json` file containing your OpenWeatherMap API key: `{"api_key": "YOUR_API_KEY"}`
2.  Run the script with `python weather_api.py`
3.  Answer the terminal prompts ( works in caps or not):
    * Enter the city name: [city]
    * Enter the country code (2 letters, e.g., FR, US, GB): [country_code]


**Please Note:**
----------


* It is essential to have an OpenWeatherMap API key to use this project. You must replace `YOUR_API_KEY` in the `key.json` file with your actual API key.
* The project generates a JSON file containing the weather information.


---


**Thank you for taking the time to test my project**


_Kenza Soopramanien - B3 Cyberschool Airbus - 2025_




