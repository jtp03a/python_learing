import requests
import os

APP_ID = os.environ.get('app_id')
API_KEY = os.environ.get('api_key')
main_endpoint = 'https://trackapi.nutritionix.com/'

headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "x-remote-user-id": "jtp03a"
    }

exercise_endpoint = f'{main_endpoint}/v2/natural/exercise'

parameters = {
        "query": "run"
    }

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)

print(response.text)


