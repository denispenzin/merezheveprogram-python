from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

async def menu(update: Update, context):
    await update.message.reply_text("Виберіть команду: /whisper або /scream")

async def whisper(update: Update, context):
    await update.message.reply_text("ти говориш дуже тихо...")

async def scream(update: Update, context):
    await update.message.reply_text("ТИ КРИЧИШЬ ДУЖЕ ГУЧНО!")

async def start(update: Update, context):
    await update.message.reply_text("Привіт! Я бот. Використовуй /menu для вибору команди.")

if __name__ == '__main__':
    app = ApplicationBuilder().token('8075070547:AAEdPoRbHWbBG4A99ZOaJQFM7ArwWQwkSWg').build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("whisper", whisper))
    app.add_handler(CommandHandler("scream", scream))

    app.run_polling()