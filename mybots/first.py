import json
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz
import random
import os

# === Константы ===
TOKEN = "8135125444:AAEfLIWp26BT1pfNiD2PYiyucYH522oFmK0"
USERS_FILE = "users.json"
HADITHS_FILE = "hadiths.txt"
TIMEZONE = pytz.timezone("Asia/Almaty")

# === Загрузка хадисов ===
def load_hadiths():
    if os.path.exists(HADITHS_FILE):
        with open(HADITHS_FILE, encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    return ["Помни об Аллахе и Аллах вспомнит о тебе."]  # запасной хадис

# === Загрузка пользователей ===
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, encoding='utf-8') as f:
            return json.load(f)
    return []

# === Сохранение пользователей ===
def save_users(users):
    with open(USERS_FILE, "w", encoding='utf-8') as f:
        json.dump(users, f)

# === Добавление нового пользователя ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    users = load_users()
    if chat_id not in users:
        users.append(chat_id)
        save_users(users)
        await update.message.reply_text("Ассаламу алейкум! ✅ Вы подписаны на хадисы и напоминания.")
    else:
        await update.message.reply_text("Вы уже подписаны 😊")

# === Сообщения ===
async def send_to_all(bot: Bot, text: str):
    users = load_users()
    for user_id in users:
        try:
            await bot.send_message(chat_id=user_id, text=text)
        except:
            pass  # например, если пользователь заблокировал бота

async def send_hadith(bot: Bot):
    hadiths = load_hadiths()
    await send_to_all(bot, f"📜 Хадис дня:\n\n{random.choice(hadiths)}")

async def send_morning_azkar(bot: Bot):
    await send_to_all(bot, "🕓 Время утренних аскаров! Не забудь упомянуть Аллаха 🙏")

async def send_evening_azkar(bot: Bot):
    await send_to_all(bot, "🌇 Время вечерних аскаров! Пусть Аллах благословит твой вечер 🤲")

# === Основной запуск ===
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    bot = Bot(token=TOKEN)

    # Команды
    app.add_handler(CommandHandler("start", start))

    # Планировщик
    scheduler = BackgroundScheduler(timezone=TIMEZONE)
    scheduler.add_job(lambda: app.create_task(send_morning_azkar(bot)), trigger='cron', hour=4, minute=30)
    scheduler.add_job(lambda: app.create_task(send_hadith(bot)), trigger='cron', hour=12, minute=0)
    scheduler.add_job(lambda: app.create_task(send_evening_azkar(bot)), trigger='cron', hour=16, minute=30)
    scheduler.start()

    print("Бот запущен...")
    app.run_polling()
