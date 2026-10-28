import os
from dotenv import load_dotenv

load_dotenv()

# Загружаем токен из .env
BOT_TOKEN = os.getenv("BOT_TOKEN")

print(f"Я прочитал токен: {BOT_TOKEN}") 