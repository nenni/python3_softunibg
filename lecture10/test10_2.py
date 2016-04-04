#!/usr/bin/env python3 -tt

"""
Въведете град: Sofia

Информация към: 04.02.2016 18:00
Температура:
Налягане: 1015
Влажност: 90%
Вятър: 7.7 м/с

    {
     'base': 'cmc stations',
     'clouds': {'all': 0},
     'cod': 200,
     'coord': {'lat': 42.7, 'lon': 23.32},
     'dt': 1455555298,
     'id': 727011,
     'main': {'grnd_level': 932.8,
              'humidity': 56,
              'pressure': 932.8,
              'sea_level': 1027.76,
              'temp': 287.064,
              'temp_max': 287.064,
              'temp_min': 287.064},
     'name': 'Sofia',
     'sys': {'country': 'BG',
             'message': 0.0042,
             'sunrise': 1455513829,
             'sunset': 1455551908},
     'weather': [{'description': 'Sky is Clear',
                  'icon': '01n',
                  'id': 800,
                  'main': 'Clear'}],
     'wind': {'deg': 216.5, 'speed': 5.57}
     }

"""

import sys
from datetime import datetime, timezone
from pprint import pprint
import requests
from datetime import datetime

# http://api.openweathermap.org/data/2.5/weather?appid=965acdac1ae64cf06761bb563ad34d96&q=sofia

API_URL = 'http://api.openweathermap.org/data/2.5/weather'
API_TOKEN = '965acdac1ae64cf06761bb563ad34d96'
API_TIMEOUT = 20
TEMP_C0_KELVIN = 273.15


def main():

    try:
        print("Your weather forecast")
        city_name = input("Enter city: ")
        # city_name = 'London,UK'
        print("Information loading...")

        if city_name:
            response = requests.get(
                API_URL,
                timeout=API_TIMEOUT,
                params={'appid': API_TOKEN, 'q': city_name}
            )

        resp = response.json()
        # pprint(resp)

        resp_dt = datetime.fromtimestamp(resp.get('dt', None), tz=timezone.utc)
        resp_main = resp.get('main', None)
        resp_main_temp_in_k = resp_main.get('temp', None)

        if resp_main_temp_in_k:
            temp_in_c = resp_main_temp_in_k - TEMP_C0_KELVIN
            # print(temp_in_c)

        resp_main_pressure = resp_main.get("pressure", None)
        resp_main_humidity = resp_main.get("humidity", None)

        resp_wind = resp.get('wind', None)
        resp_wind_speed = resp_wind.get('speed', None)

        print()
        print("Date: {}".format(resp_dt.strftime('%d-%m-%Y %H:%M')))
        print("""Temp: {temp:.2f}C
Pressure: {pressure}
Humidity: {humidity}%
Wind speed: {wind} m/s""".format(
            temp=temp_in_c,
            pressure=resp_main_pressure,
            humidity=resp_main_humidity,
            wind=resp_wind_speed
        ))

        return 0
    except Exception as e:
        print("Error: " + str(e))
        return 1


if __name__ == "__main__":
    sys.exit(main())
