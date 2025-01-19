import requests, os
from dotenv import load_dotenv

load_dotenv

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

response = requests.get(f"https://api.groupme.com/v3/groups?token={ACCESS_TOKEN}")

if response.status_code == 200:
    print(response.json()['response'])
    groups = response.json()['response']

    for group in groups:
        name = group['name']
        id = group['id']
        print(f'Name: {name}, ID: {id}')
else:
    print('Failed to get groups')