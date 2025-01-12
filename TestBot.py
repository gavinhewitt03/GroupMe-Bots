import requests, os
from datetime import datetime as dt, timedelta
from dotenv import load_dotenv

load_dotenv()
api_url = 'https://api.groupme.com/v3/bots/post'

if dt.now().date() == dt(2025, 1, 12).date():
    bot_text = 'Your workflow identified that it was today!'
else:
    bot_text = 'Your workflow did not run as intended. Try again :('


data = {
    'bot_id': os.getenv('TEST_BOT_ID'),
    'text': bot_text
}

requests.post(api_url, json=data)
