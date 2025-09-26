import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Взимаме BOT_TOKEN от ENV
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Тук можеш да сложиш твоя CHANNEL_ID, ако искаш да пращаш автоматични сигнали
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Здравей! Аз съм твоят трейдинг бот. 🚀")

# Примерна команда /signal
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Тук можеш да извикаш твоята логика за сигнали
    message = "📈 EUR/USD Buy 0.12 lots\nTP: 4 pips\nSL: 2 pips"
    await update.message.reply_text(message)

    # Ако искаш да пращаш и в канал:
    if CHANNEL_ID:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=message)

# Главна функция
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Регистрация на команди
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("signal", signal))

    # Стартиране на бота
    application.run_polling()

if __name__ == "__main__":
    main()
