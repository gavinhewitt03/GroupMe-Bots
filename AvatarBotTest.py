import requests, os
from dotenv import load_dotenv

load_dotenv()
api_url = 'https://api.groupme.com/v3/bots/post'

bot_text = f'Hopefully I have a custom avatar!'


data = {
    'bot_id': os.getenv('AVATAR_BOT_ID'),
    'text': bot_text
}

response = requests.post(api_url, json=data)
