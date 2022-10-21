import requests
import os
import datetime

USERNAME = 'jtp03a'
TOKEN = os.environ.get('pixela_token')

pixela_endpoint = 'https://pixe.la/v1/users'

# Create User
parameters = {
  'token': TOKEN,
  'username': USERNAME,
  'agreeTermsOfService': 'yes',
  'notMinor': 'yes'
}
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

# Create Graph
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
  'id': 'graph1',
  'name': 'Cycle Graph',
  'unit': 'mi',
  'type': 'float',
  'color': 'sora'
}

headers = {
  "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Post Pixel
pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}'

current_date = datetime.date.today()
current_date_formated = current_date.strftime("%Y%m%d")
print(current_date_formated)

pixel_params = {
  'date': current_date_formated,
  'quantity': '10'
}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

# Update Pixel - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
update_pixel = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}/{current_date_formated}'

update_params = {
  'quantity': '20'
}

# response = requests.put(url=update_pixel, json=update_params, headers=headers)
# print(response.text)

# Delete Pixel - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
delete_pixel = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}/{current_date_formated}'

response = requests.delete(url=delete_pixel, headers=headers)
print(response.text)



