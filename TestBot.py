import requests, os
from datetime import datetime as dt, timedelta
from dotenv import load_dotenv

load_dotenv()
api_url = 'https://api.groupme.com/v3/bots/post'

print('HI! THIS IS RUNNING!')

bot_text = f'You scheduled this to run at 11:35. It is currently {dt.now()}.'


data = {
    'bot_id': os.getenv('TEST_BOT_ID'),
    'text': bot_text
}

response = requests.post(api_url, json=data)
