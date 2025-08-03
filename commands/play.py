# 👋 Здесь мы подключаем нужные части из библиотеки telegram
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, ContextTypes, filters

# 🎲 Импортируем модуль random, чтобы выбирать случайный вариант
import random

# ✅ Задание для тебя:
# Напиши список из трёх слов: "камень", "ножницы", "бумага"
# Это варианты, которые может выбрать игрок и бот
choices = ["камень", "ножницы", "бумага"]

# 🟢 Когда пользователь напишет команду /play, сработает эта функция
# Задание: Попроси пользователя выбрать камень, ножницы или бумагу
async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Выбери: камень, ножницы или бумага")

# 🟡 Эта функция будет срабатывать, когда игрок напишет слово (например "камень")
async def play_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 📌 Сохраняем, что написал игрок, и делаем все буквы маленькими
    user_choice = update.message.text.lower()

    # ⛔ Если игрок написал что-то странное, просто выходим
    if user_choice not in choices:
        return

    # 🎯 Бот случайно выбирает свой вариант
    bot_choice = random.choice(choices)

    # 💭 Считаем, кто победил — ты или бот
    result = decide(user_choice, bot_choice)

    # 💬 Отправляем игроку, кто кого победил
    await update.message.reply_text(
        f"Ты выбрал: {user_choice}\nЯ выбрал: {bot_choice}\nРезультат: {result}"
    )

# 🔍 Эта функция решает, кто победил
# Задание: попробуй сама придумать, как определить победителя!
# Подсказка: камень бьёт ножницы, ножницы бьют бумагу, бумага бьёт камень
def decide(user: str, bot: str) -> str:
    if user == bot:
        return "Ничья!"  # если одинаково — никто не победил

    # 👉 Словарь, где написано кто кого побеждает
    wins = {
        "камень": "ножницы",
        "ножницы": "бумага",
        "бумага": "камень",
    }

    if wins[user] == bot:
        return "Ты победил!"
    else:
        return "Я победил!"

# 📦 Эти штуки подключаются в главный файл bot.py
play_command_handler = CommandHandler("play", play_command)
play_choice_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), play_choice)
