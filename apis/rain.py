import requests
from twilio.rest import Client
import os

api_key = os.environ.get('openweather_key')
endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
MY_LAT = os.environ.get('mylat')
MY_LONG = os.environ.get('mylon')
account_sid = os.environ.get('twilio_sid')
auth_token = os.environ.get('twilio_token')

weather_params = {
  'lat': MY_LAT,
  'lon': MY_LONG,
  'appid': api_key,
  'exclude': 'current,minutely,daily'
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()

next_12hrs = weather_data['hourly'][:12]

for hour in next_12hrs:
  if hour['weather'][0]['id'] >= 700:
    print('Bring an umbrella')

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Its going to rain, bring an umbrella",
                        from_=os.environ.get('twilio_num'),
                        to=os.environ.get('twilio_mynum')
                    )

    print(message.status)
    break



