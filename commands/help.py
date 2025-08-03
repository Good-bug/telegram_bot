# 📦 Импортируем нужные штуки из библиотеки Telegram
from telegram import Update  # 💬 Сообщения от пользователей
from telegram.ext import CommandHandler, ContextTypes  # 🧠 Командные помощники

# 🆘 Когда пользователь пишет /help, вызывается эта функция
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 📋 Отправляем список доступных команд
    await update.message.reply_text(
        "📚 Команды, которые я понимаю:\n"
        "/start — поздороваться 👋\n"
        "/help — показать эту подсказку 🆘\n"
        "/play — сыграть в камень-ножницы-бумага ✊✋✌️"
    )

# 🧩 Создаём обработчик команды /help
# 🔄 Он будет запускать функцию help_command, когда кто-то напишет /help
help_handler = CommandHandler("help", help_command)
