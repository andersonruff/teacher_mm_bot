import requests
import random
from datetime import datetime

TOKEN = ""
CHAT_ID = ""

QUESTIONS = [
    "What is your name?",
    "Where are you from?",
    "What did you do yesterday?",
    "Describe your daily routine."
]

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

question = random.choice(QUESTIONS)

message = (
    "🇬🇧 English Practice\n\n"
    f"{question}\n\n"
    f"⏰ {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}"
)

send_telegram(message)
