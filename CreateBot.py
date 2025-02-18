import requests, os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

url = f"https://api.groupme.com/v3/bots?token={ACCESS_TOKEN}"

GROUP_ID = os.getenv("GROUP_ID")
BOT_NAME = os.getenv("BOT_NAME")

data = {
    'bot': {
        'name': BOT_NAME,
        'group_id': GROUP_ID
    }   
}

response = requests.post(url, json=data)
print(response.json())