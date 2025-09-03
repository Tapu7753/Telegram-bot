import telebot

# Aapka bot token
TOKEN = "8054738355:AAHhEdV0n8fIZ4X_keT21-zEzqAAnfqZIak"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ Hello 👋, My test bot

I can store private files in Specified Channel and other users can access it from special link..")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Aapne bola: " + (message.text or ""))

bot.infinity_polling()
