import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler
)

from handlers.start_handler import start
from dotenv import load_dotenv
import os
from pathlib import Path

from handlers.callback_handler import callback_handler
from handlers.message_handler import message_handler

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)


TOKEN_BOT = os.getenv('BOT_TOKEN')


if __name__ == '__main__':

    application = ApplicationBuilder().token(TOKEN_BOT).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT, message_handler))
    # application.add_handler(MessageHandler(filters.CONTACT, phonenumber_handler))
    application.add_handler(CallbackQueryHandler(callback_handler))
    
    application.run_polling()
