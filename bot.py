import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! به ربات MMN خوش آمدی.\n\n"
        "برای مشاهده راهنما، دستور /help را ارسال کن."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "دستورات ربات:\n"
        "/start - شروع کار با ربات\n"
        "/help - نمایش راهنما\n\n"
        "هر پیام متنی دیگری را نیز برای ربات ارسال کن."
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"پیام شما دریافت شد:\n{update.message.text}"
    )


def main():
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN is not set. Please configure it in the .env file."
        )

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    )

    print("MMN Telegram Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
