from telegram.ext import ApplicationBuilder, CommandHandler

app = ApplicationBuilder().token("7786341898:AAHdPjculC44KfjYmVyjvbloEgkfaCmkGwE").build()

# Example: /start command
async def start(update, context):
    await update.message.reply_text("Hello, I'm alive!")

app.add_handler(CommandHandler("start", start))

app.run_polling()
