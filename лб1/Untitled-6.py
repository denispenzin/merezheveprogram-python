import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def menu(update: Update, context: CallbackContext) -> None:
    menu_text = (
        "Команди:\n"
        "/menu - Показати меню\n"
        "/whisper <текст> - Тихо сказати текст\n"
        "/scream <текст> - Голосно сказати текст"
    )
    update.message.reply_text(menu_text)

def whisper(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    if text:
        update.message.reply_text(text.lower())
    else:
        update.message.reply_text("Введіть текст для тихого шепоту.")

def scream(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    if text:
        update.message.reply_text(text.upper())
    else:
        update.message.reply_text("Введіть текст для крику.")

def error(update: Update, context: CallbackContext) -> None:
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')

def main() -> None:
    """Start the bot."""
    token = '7841321216:AAGXtTEGd5xdG_byCJhsMJBstppcwvgHx_w' 

    updater = Updater(token, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("menu", menu))
    dispatcher.add_handler(CommandHandler("whisper", whisper))
    dispatcher.add_handler(CommandHandler("scream", scream))
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
