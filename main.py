from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
from questions import QUESTIONS

TOKEN = 8870283231:AAFMNV7TPf-_iBMbgXxOA71sm4Goy_wNyaU

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот для подготовки к меду 🩺\n"
        "Команда /question — получить случайный вопрос"
    )

async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = random.choice(QUESTIONS)
    await update.message.reply_text(q)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("question", question))

app.run_polling()
