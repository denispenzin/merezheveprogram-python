import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Встановлюємо рівень логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Функція, що обробляє команду /menu
def menu(update: Update, context: CallbackContext) -> None:
    menu_text = (
        "Команди:\n"
        "/menu - Показати меню\n"
        "/whisper <текст> - Тихо сказати текст\n"
        "/scream <текст> - Голосно сказати текст"
    )
    update.message.reply_text(menu_text)

# Функція, що обробляє команду /whisper (перетворює текст на маленькі літери)
def whisper(update: Update, context: CallbackContext) -> None:
    # Отримати текст після команди /whisper
    text = ' '.join(context.args)
    if text:
        update.message.reply_text(text.lower())
    else:
        update.message.reply_text("Введіть текст для тихого шепоту.")

# Функція, що обробляє команду /scream (перетворює текст на великі літери)
def scream(update: Update, context: CallbackContext) -> None:
    # Отримати текст після команди /scream
    text = ' '.join(context.args)
    if text:
        update.message.reply_text(text.upper())
    else:
        update.message.reply_text("Введіть текст для крику.")

# Функція для обробки помилок
def error(update: Update, context: CallbackContext) -> None:
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')

# Основна функція для запуску бота
def main() -> None:
    """Start the bot."""
    # Токен вашого бота
    token = '7841321216:AAGXtTEGd5xdG_byCJhsMJBstppcwvgHx_w'  # Заміни на свій токен бота

    # Створюємо Updater та передаємо йому токен вашого бота
    updater = Updater(token, use_context=True)

    # Отримуємо диспетчер для реєстрації обробників команд
    dispatcher = updater.dispatcher

    # Реєструємо команди
    dispatcher.add_handler(CommandHandler("menu", menu))
    dispatcher.add_handler(CommandHandler("whisper", whisper))
    dispatcher.add_handler(CommandHandler("scream", scream))

    # Реєстрація обробника для помилок
    dispatcher.add_error_handler(error)

    # Запускаємо бота
    updater.start_polling()

    # Запуск відбуватиметься до зупинки користувачем
    updater.idle()

if __name__ == '__main__':
    main()
