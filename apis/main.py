# Response Codes Easy to Remember
# 1XX: Hold On
# 2XX Here you go
# 3XX: Go away
# 4XX: You Screwed Up
# 5XX: I screwed Up

import requests
from datetime import datetime

MY_LAT = 29.430970
MY_LONG = -98.769660

iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response = requests.get(url='https://api.kanye.rest')

parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

sun_response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)

iss_response.raise_for_status()
sun_response.raise_for_status()

iss_data = iss_response.json()
sun_data = sun_response.json()

def get_hour(iso_string):
    hour = iso_string.split('T')[1].split(':')[0]
    return hour

def iss_in_range(iss_lat, iss_long, my_lat, my_long):
    lat_diff = abs(iss_lat - my_lat)
    print(lat_diff)
    long_diff = abs(iss_long - my_long)
    print(long_diff)
    if lat_diff <= 5 and long_diff <= 5:
        return True
    else:
        return False

def is_night(sunset, sunrise):
    time_now = datetime.now()
    if time_now.hour <= sunrise and time_now.hour >= sunset:
        return True
    else:
        return False

sunrise_hour = int(get_hour(sun_data['results']['sunrise']))
sunset_hour = int(get_hour(sun_data['results']['sunset']))
iss_lat = float(iss_data['iss_position']['latitude'])
iss_long = float(iss_data['iss_position']['longitude'])


if iss_in_range(iss_lat, iss_long, MY_LAT, MY_LONG) and is_night(sunset_hour, sunrise_hour):
    print('ISS is visible')
else:
    print('ISS is not visible')






