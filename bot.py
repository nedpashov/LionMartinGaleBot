import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command."""
    await update.message.reply_text("LionMartingaleBot is running! Use /help for more info.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /help command."""
    await update.message.reply_text("Available commands:\n/start - Start the bot\n/help - Show this message")

async def send_to_channel(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a periodic message to the specified channel."""
    await context.bot.send_message(chat_id=CHANNEL_ID, text="LionMartingaleBot is alive!")

def main() -> None:
    """Run the bot."""
    if not BOT_TOKEN or not CHANNEL_ID:
        print("Error: BOT_TOKEN or CHANNEL_ID not set in environment variables.")
        return

    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Schedule periodic message to channel every 60 seconds
    application.job_queue.run_repeating(send_to_channel, interval=60, first=10)

    # Start the bot
    print("Bot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
