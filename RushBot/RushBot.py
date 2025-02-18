import requests, os
from dotenv import load_dotenv
from datetime import datetime as dt

load_dotenv()

API_URL = 'https://api.groupme.com/v3/bots/post'
BOT_ID = os.getenv("BOT_ID")

RUSH_DATES = {
    'Info&Comm': dt(2025, 1, 27).date(),
    'Workshop': dt(2025, 1, 28).date(),
    'Mixer': dt(2025, 1, 29).date(),
    'SD': dt(2025, 1, 30).date(),
    'PD': dt(2025, 2, 3).date()
}

today = dt.now().date()

BOT_MESSAGES = {
    RUSH_DATES['Info&Comm']:
        'Happy Monday, all! Tonight is our rescheduled Info Night merged with our Committee Fair. '
        'At this event, you\'ll get to learn more about our fraterntiy and hear from '
        'each of our chairs about their positions and the committees they oversee. After the presentation, '
        'you\'ll have the opportunity to network with brothers, ask brothers and chairs questions, and '
        'have free pizza!\n'
        '\nWhere: Swearingen 1C01 (Amoco Hall)'
        '\nWhen: 7:30PM, arrive at least 20 minutes early for check-in'
        '\nDress Code: Casual'
        '\nWhat to Bring: Yourself!',
    RUSH_DATES['Workshop']:
        'Hello! Come on out for a night of professional development with our brothers. '
        'In this business casual rush event, brothers will help you work on your professional skills. '
        'This workshop covers essential topics such as resume improvement, LinkedIn optimization, and mock interviews, '
        'as well as research and internship panels to elevate your career readiness.\n'
        '\nWhere: 300 Main Lobby'
        '\nWhen: 7:30PM, arrive early for check-in'
        '\nDress Code: Business Casual'
        '\nWhat to Bring: 5 copies of your resume',
    RUSH_DATES['Mixer']:
        'Good morning, everyone! Tonight, we are showcasing a brand new event, the Professional Mixer. '
        'Get ready to network with brothers in a low stakes casual, professional manner at this event.\n'
        '\nWhere: 300 Main Lobby'
        '\nWhen: 7:30PM, arrive early for check-in'
        '\nDress Code: Business Casual'
        '\nWhat to Bring: Water!',
    RUSH_DATES['SD']:
        'Good morning! Tonight is our final rush event before Professional Dinner, Speed Dating. '
        'A pivotal event in the recruitment process, Speed Dating offers an opportunity for one-on-one interactions '
        'with each brother through a series of quick conversations. This event is long, so prepare for around 2 hours of talking. '
        'Attending this event is mandatory to be considered for an invite to Professional Dinner and a bid.\n'
        '\nWhere: Swearingen Lobby'
        '\nWhen: 7:00PM, arrive early for check-in'
        '\nDress Code: Casual'
        '\nWhat to Bring: Water!'
}

if today in BOT_MESSAGES and today != RUSH_DATES['Workshop']:
    bot_text = BOT_MESSAGES[today]

    data = {
        'bot_id': BOT_ID,
        'text': bot_text
    }

    response = requests.post(API_URL, json=data)
    print(response.text)
        