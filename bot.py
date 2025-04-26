from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Your command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I'm alive!")

# Main function
def main():
    app = ApplicationBuilder().token("7786341898:AAHdPjculC44KfjYmVyjvbloEgkfaCmkGwE").build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == '__main__':
    main()
