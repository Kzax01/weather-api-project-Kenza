**🌤️ Welcome to my OpenWeatherMap Weather Forecast Project**


This is a python script that fetches a 5 day weather forecasts from OpenWeatherMap and analyzes precipitation patterns and major weather transitions.

## 📋 Features

- Retrieves 5-day weather forecasts with 3-hour intervals
- Calculates daily rainfall and snowfall accumulation
- Detects major weather transitions (weather category change + temperature variation > 3°C)
- Generates a structured JSON report
- User-friendly command-line interface

## 🛠️ Prerequisites

- Python 3.7 or higher
- An OpenWeatherMap API key ([Get it here for free](https://openweathermap.org/api))

## 📥 Installation

### Method 1: Download ZIP from GitHub

1. Click the green **"Code"** button at the top of this repository
2. Select **"Download ZIP"**
3. Extract the ZIP file to your desired location

## ⚙️ Setup

### Step 1: Create a virtual environment (recommended)

**On Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure your API key

1. Open the `key.json` file
2. Replace `"ENTER_YOUR_KEY"` with your actual OpenWeatherMap API key:
```json
{
    "API_KEY": "your_actual_api_key_here"
}
```

⚠️ **Important:** Never share your real API key publicly!

## 🚀 Usage

1. Make sure your virtual environment is activated
2. Run the script:
```bash
python weather_api.py
```

3. Follow the prompts:
   - Enter a city name (e.g., `Paris`, `London`, `Tokyo`)
   - Enter a 2-letter country code, in caps or not it's ok. (e.g., `FR`, `GB`, `JP`)

4. The script will generate a `result.json` file with the weather analysis

## 🔍 What are "Major Transitions"?

A major transition occurs when **both** conditions are met between two consecutive 3-hour forecasts:

1. Weather category changes (e.g., Clear → Rain, Clouds → Snow)
2. Temperature varies by more than 3°C (in absolute value)

## 📦 Project Structure
```
weather-forecast-project/
│
├── weather_api.py          # Main script
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── key.json               # API key configuration
└── result.json            # Generated output (after running)
```

## 🐛 Troubleshooting

### "Error: code 401"
- Check that your API key is correctly configured in `key.json`
- Verify your API key is valid on [OpenWeatherMap](https://openweathermap.org/api_keys)

### "Unable to retrieve data"
- Verify your internet connection
- Check the city name and country code are correct
- Some small cities might not be in the OpenWeatherMap database

### Import errors
- Make sure you've activated your virtual environment
- Run `pip install -r requirements.txt` again

## 📝 Notes

- The API provides forecasts in 3-hour intervals, which may result in partial data for the first and last days
- All temperatures are in Celsius
- Precipitation is measured in millimeters (mm)

## 👤 Author

Kenza Soopramanien - B3 Cyberschool Airbus - 2025

## 📄 License

This project is for educational purposes as part of a school assignment.
