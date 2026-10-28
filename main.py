import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage # Пока храним состояния в памяти

from config import BOT_TOKEN
from handlers import start # Импортируем наш роутер

# Настройка логирования (чтобы видеть ошибки в консоли)
logging.basicConfig(level=logging.INFO)

async def main():
    # Инициализируем бота и диспетчер
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    
    # Подключаем роутеры (обработчики)
    dp.include_router(start.router)
    # dp.include_router(pet.router) # Добавим, когда напишем
    
    print("Бот запущен и ждет сообщений...")
    # Запускаем бота (пропускаем старые обновления, чтобы не спамить при перезапуске)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен.")