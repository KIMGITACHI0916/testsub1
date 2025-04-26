from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text('Hello! I am alive!')

app = ApplicationBuilder().token("7786341898:AAHdPjculC44KfjYmVyjvbloEgkfaCmkGwE").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
