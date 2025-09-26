import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Взимаме токена и канала от ENV
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# /start команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Ботът е стартиран и работи 24/7 в Render!")

# /signal команда – праща сигнал в чата + в канала
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "📈 EUR/USD Buy 0.12 lots\nTP: 4 pips\nSL: 2 pips"
    await update.message.reply_text("✅ Сигналът е изпратен!")

    # Праща в канал
    if CHANNEL_ID:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=message)

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Регистрация на командите
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("signal", signal))

    # Стартиране
    application.run_polling()

if __name__ == "__main__":
    main()
