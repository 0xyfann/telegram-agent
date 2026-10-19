import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from anthropic import Anthropic

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]

claude = Anthropic(api_key=ANTHROPIC_API_KEY)

async def balas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan_user = update.message.text
    respons = claude.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1000,
        messages=[{"role": "user", "content": pesan_user}],
    )
    await update.message.reply_text(respons.content[0].text)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, balas))
app.run_polling()
