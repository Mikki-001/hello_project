"""Entrypoint for Telegram bot application."""

from __future__ import annotations

import os

from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from bot.handlers import help_command, quiz_command, start_command, text_message, word_command


def create_application() -> Application:
    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set. Fill .env file first.")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("word", word_command))
    app.add_handler(CommandHandler("quiz", quiz_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_message))
    return app


def main() -> None:
    app = create_application()
    app.run_polling()


if __name__ == "__main__":
    main()
