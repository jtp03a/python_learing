import os
import requests
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc OR Tesla"
STOCK_API_KEY = os.environ.get('stocks_api_key')
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_API_KEY = os.environ.get('news_api_key')
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
TWILIO_SID = os.environ.get('twilio_sid')
TWILIO_TOKEN = os.environ.get('twilio_token')

class News_Manager:
  def __init__(self):
    self.params = {
      'qInTitle': COMPANY_NAME,
      'from': current_date_iso,
      'to': f'{year}-{month}-{day_before}',
      'apiKey': NEWS_API_KEY,
      'sortBy': 'popularity'
    }

  def getnews(self, num_results):  
    self.response = requests.get(NEWS_ENDPOINT, params=self.params)
    self.response.raise_for_status()
    self.response_json = self.response.json()
    self.response_str = ''

    for article in self.response_json['articles'][:num_results]:
      self.response_str += f"Headline: {article['title']} \nBrief: {article['content']}\n"
    
    print(self.response_str)
    return self.response_str

class Stock_Manager:
  def __init__(self):
    self.params = {
      'function' : 'TIME_SERIES_DAILY',
      'symbol': STOCK,
      'outputsize': 'full',
      'apikey': STOCK_API_KEY
    }

  def getstocks(self):
    self.response = requests.get(STOCK_ENDPOINT, params=self.params)
    self.response.raise_for_status()
    self.response_json = self.response.json()

    close_yesterday = float(self.response_json['Time Series (Daily)'][f'{year}-{month}-{yesterday}']['4. close'])
    close_day_before = float(self.response_json['Time Series (Daily)'][f'{year}-{month}-{day_before}']['4. close'])

    change = round(close_yesterday - close_day_before, 2)

    sign: str

    if change < 0:
      sign = '🔻'
    else:
      sign = '🔺'

    if abs(change) > 5:
      self.message = f'{STOCK}: {sign}{abs(change)}\n'
      print(self.message)
      self.message += news_manager.getnews(3)
      # sms_manager.send_alert(self.message)

class SMS_Manager:
  def __init__(self):
    self.client = Client(TWILIO_SID, TWILIO_TOKEN)
  
  def send_alert(self, message):
    message = self.client.messages \
                .create(
                    body=message,
                    from_=os.environ.get('twilio_num'),
                    to=os.environ.get('twilio_mynum')
                )

    print(message.status)


current_date = datetime.date.today()
current_date_iso = datetime.date.today().isoformat().split('T')[0]

month = current_date.strftime('%m')
year = current_date.strftime('%Y')
today = int(current_date.strftime('%d'))
yesterday = int(current_date.strftime('%d')) - 1
day_before = int(current_date.strftime('%d')) - 2

news_manager = News_Manager()
stock_manager = Stock_Manager()
# sms_manager = SMS_Manager()
stock_manager.getstocks()

