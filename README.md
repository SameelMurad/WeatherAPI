<<<<<<< HEAD
# **Weather Data Logger**

This Python script retrieves real-time weather data for a given city using the [OpenWeatherMap API](https://openweathermap.org/api) and logs it to a CSV file at regular intervals.  

It’s ideal for **data collection projects**, **climate analysis**, or **personal weather tracking**.

---

## **Features**
- Fetches real-time weather data (temperature, humidity, wind speed, description, etc.)
- Automatically converts temperatures from Kelvin to Celsius
- Logs results with timestamps to a CSV file
- Runs continuously, collecting data every hour
- Easy configuration with `.env` for secure API key storage

---

## **Requirements**
- Python 3.8+
- An OpenWeatherMap API key ([Sign up here](https://home.openweathermap.org/users/sign_up))
- Required Python packages:
  - `pandas`
  - `requests`
  - `python-dotenv`

---

## **Installation**
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/weather-data-logger.git
   cd weather-data-logger
2. **Install Dependencies**
   ```bash
   pip install pandas requests python-dotenv
3. Set up your `.env` file
   `API_key=your_openweathermap_api_key`
   *Note: the script reads os.getenv('API_key'), so keep the variable name API_key*

## **Usage**
1. Edit the script to set the desired location (example):
    ```python
    `city_name = "Birmingham"`
    `country_code = "UK`
    *Tip: OpenWeatherMap uses ISO 3166 country codes; for the United Kingdom you can also use GB.*
2. Run the script:
    ```bash
    python3 weather_logger.py
3. What happens:
    - The script fetches the latest weather data
    - Appends it to weather_data.csv
    - Sleeps for one hour and repeats (changeable via time.sleep(...))
4. Stop the script with `Ctrl + C`.

## **Example CSV Output**
| timestamp           | city       | country | temperature | feels\_like | humidity | description      | wind\_speed |
| ------------------- | ---------- | ------- | ----------- | ----------- | -------- | ---------------- | ----------- |
| 2025-08-10 14:00:00 | Birmingham | GB      | 18.23       | 17.10       | 64       | scattered clouds | 3.5         |

## **Customisation**

- **Change Collection Interval**: edit the sleep duration (seconds) near the end of the script:
    ```python
    `time.sleep(3600)` #3600 seconds = 1 hour
- **Change output filename**: call `save_weather_data(result, filename="my_weather_log.csv")`

## **Security & Good Practices**
- Keep your `.env` file out of verstion control. Add `.env` to `.gitignore`.
- Use a virtual environment (venv, pipenv) for dependency isolation.
=======
This project has 3 main steps

Step 1: Get weather data from the OpenWeatherMap API

Step 2: Analyse and process the data to get the relevant information

Step 3: Recommend whether or not someone should wear a coat today

>>>>>>> 01a264e1ef52e03935358717baeecc0828d864dc
