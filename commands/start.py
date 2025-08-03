# 📦 Импортируем нужные штуки из библиотеки Telegram
from telegram import Update  # 💬 Это сообщение, которое пишет пользователь
from telegram.ext import CommandHandler, ContextTypes  # 🧠 Помогают нам обрабатывать команды

# 🌟 Эта функция сработает, когда кто-то напишет /start в Telegram
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 💌 Отвечаем человеку в чат фразой ниже
    await update.message.reply_text(
        "Привет! 👋 Я играю в камень, ножницы, бумага ✊✋✌️\nНапиши /play чтобы начать игру!"
    )

# 🧩 Создаём "обработчик" (handler) для команды /start
# 📥 Он говорит боту: "Если кто-то напишет /start — запусти функцию выше!"
start_handler = CommandHandler("start", start)
