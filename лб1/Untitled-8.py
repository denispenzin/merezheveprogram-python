from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

async def start(update: Update, context):
    keyboard = [[KeyboardButton("Menu")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Привіт! Натисни 'Menu' для вибору.", reply_markup=reply_markup)

async def menu(update: Update, context):
    if update.message.text == "Menu":
        keyboard = [[KeyboardButton("Whisper"), KeyboardButton("Scream")]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Виберіть 'Whisper' або 'Scream':", reply_markup=reply_markup)

async def handle_choice(update: Update, context):
    text = update.message.text
    if text == "Whisper":
        await update.message.reply_text("ти говориш дуже тихо...")
    elif text == "Scream":
        await update.message.reply_text("ТИ КРИЧИШЬ ДУЖЕ ГУЧНО!")
    else:
        await update.message.reply_text("Натисни 'Menu' для вибору.")

if __name__ == '__main__':
    app = ApplicationBuilder().token('8075070547:AAEdPoRbHWbBG4A99ZOaJQFM7ArwWQwkSWg').build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex('^Menu$'), menu))
    app.add_handler(MessageHandler(filters.Regex('^(Whisper|Scream)$'), handle_choice))
    app.run_polling()
