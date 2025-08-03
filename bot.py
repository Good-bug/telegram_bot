# 🐍 Импортируем нужные части из библиотеки для Телеграма
from telegram.ext import Application
from commands.play import play_command_handler, play_choice_handler

# 🌿 Импортируем dotenv, чтобы читать токен из .env файла
from dotenv import load_dotenv
import os

# 📂 Загружаем .env файл
load_dotenv()

# 🔑 Получаем токен из переменной окружения
token = os.getenv("BOT_TOKEN")

# 🧠 Это асинхронная функция — она запустит нашего бота!
async def main():
    if not token:
        print("❌ Токен не найден. Убедись, что есть файл .env с переменной BOT_TOKEN.")
        return

    # 🤖 Создаём приложение (это как сам бот)
    app = Application.builder().token(token).build()

    # 🧩 Подключаем команды (ты сама уже их писала!)
    app.add_handler(play_command_handler)  # /play — начать игру
    app.add_handler(play_choice_handler)   # текст после /play

    # 🚀 Запускаем бота — он будет ждать сообщения
    print("✅ Бот запущен! Нажимай /play в Telegram")
    await app.run_polling()

# 🏁 Эта строчка запускает main
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
