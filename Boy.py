import os
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def delete_later(message):
    await asyncio.sleep(300)
    try:
        await message.delete()
    except Exception as e:
        print(e)

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.video:
        sent = await update.message.reply_video(
            video=update.message.video.file_id,
            caption="⏳ This video will be deleted in 5 minutes."
        )
        asyncio.create_task(delete_later(sent))

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.VIDEO, handle_video))

print("Bot is running...")
app.run_polling()
