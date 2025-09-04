from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7565526262:AAFFpo9RtjiFN5LWmKkGkLSMTMCqF1EGXtU"
ADMINS = [@Tapuugk]  # Apna Telegram user ID daalo

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot chal raha hai!")

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id not in ADMINS:
        await update.message.reply_text("❌ Sirf admin use kar sakta hai")
        return
    if not update.message.reply_to_message:
        await update.message.reply_text("Reply karke /ban likho")
        return
    user_id = update.message.reply_to_message.from_user.id
    await update.effective_chat.ban_member(user_id)
    await update.message.reply_text("🚫 User banned!")

async def unban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id not in ADMINS:
        await update.message.reply_text("❌ Sirf admin use kar sakta hai")
        return
    if len(context.args) == 0:
        await update.message.reply_text("Usage: /unban <user_id>")
        return
    user_id = int(context.args[0])
    await update.effective_chat.unban_member(user_id)
    await update.message.reply_text("✅ User unbanned!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ban", ban))
app.add_handler(CommandHandler("unban", unban))

print("Bot chal raha hai...")
app.run_polling()
