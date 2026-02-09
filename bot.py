import os
import requests
import random
from datetime import datetime

# ===== CONFIGURAÇÃO (VINDO DOS SECRETS DO GITHUB) =====
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not TOKEN or not CHAT_ID:
    raise ValueError("BOT_TOKEN ou CHAT_ID não configurados nas variáveis de ambiente.")

# ===== BANCO DE PERGUNTAS =====
QUESTIONS = [
    "What is your name?",
    "Where are you from?",
    "What did you do yesterday?",
    "Describe your daily routine.",
    "What are your hobbies?",
    "What are your plans for the weekend?"
]

# ===== FUNÇÃO PARA ENVIAR MENSAGEM =====
def send_telegram(message: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=10
    )

    if response.status_code != 200:
        raise RuntimeError(
            f"Erro ao enviar mensagem: {response.status_code} - {response.text}"
        )

# ===== FUNÇÃO PRINCIPAL =====
def main():
    question = random.choice(QUESTIONS)

    message = (
        "🇬🇧 *English Practice*\n\n"
        f"❓ {question}\n\n"
        f"⏰ {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}"
    )

    send_telegram(message)
    print("Mensagem enviada com sucesso!")

# ===== EXECUÇÃO =====
if __name__ == "__main__":
    main()
