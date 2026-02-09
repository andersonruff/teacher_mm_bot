import os
import requests
import random
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("BOT_TOKEN:", "OK" if BOT_TOKEN else "MISSING")
print("CHAT_ID:", "OK" if CHAT_ID else "MISSING")

QUESTIONS = [
    "What is your name?",
    "Where are you from?",
    "What did you do yesterday?",
    "Describe your daily routine."
]

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

    print("Telegram status:", response.status_code)
    print("Telegram response:", response.text)

question = random.choice(QUESTIONS)

message = (
    "🇬🇧 English Practice\n\n"
    f"{question}\n\n"
    f"⏰ {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}"
)

send_telegram(message)
