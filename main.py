import telebot,os,time
from keep_alive import keep_alive
keep_alive()

BOT_TOKEN = "7399774608:AAExFx2rNd_LYCBfTHGDMQWpzBFs7JFFm4U"
botRunning = True

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Xin chào! Tôi là bot Telegram của bạn.")

bot.infinity_polling()
