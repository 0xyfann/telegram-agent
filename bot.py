import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from groq import Groq

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
GROQ_API_KEY = os.environ["GROQ_API_KEY"]

ai = Groq(api_key=GROQ_API_KEY)

async def balas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan_user = update.message.text
    respons = ai.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1000,
        messages=[{"role": "user", "content": pesan_user}],
    )
    await update.message.reply_text(respons.choices[0].message.content)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, balas))
app.run_polling()
