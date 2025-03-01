import telebot,os,time
bot = telebot.TeleBot("7384250892:AAHKP4H-Bbao773rN_oxF9lp41W3OGoF_m8", parse_mode="HTML")
ADMIN_ID = [6481553299]

@bot.message_handler(commands=['onbot'])
def offbot(message):
    if (message.from_user.id in ADMIN_ID):
        bot.reply_to(message, "Bot ã bt")
        bot.stop_polling()

bot.infinity_polling()
os.system("python main.py")