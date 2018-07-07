import requests
from decouple import config


TOKEN = config('TOKEN')


def send_message(text, chat_id):
    data = {'chat_id': chat_id, 'text': text}
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)
    requests.post(url, data = data)
