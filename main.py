import telebot,os,time
from keep_alive import keep_alive
keep_alive()

bot = telebot.TeleBot("7384250892:AAHKP4H-Bbao773rN_oxF9lp41W3OGoF_m8", parse_mode="HTML")
file_acc = "pqhsave.json"
ADMIN_ID = [6481553299]

@bot.message_handler(commands=['start', 'help'])
def ds_lenh(message):
	text = '''
PHAN QUOC HUY BOT
=================
Danh sách các lệnh
=================
/help - Xem lệnh
/tx - comming soon
ADMIN:
/offbot - Tắt bot
/onbot - Bật bot
'''
	bot.reply_to(message, text);

@bot.message_handler(commands=['offbot'])
def offbot(message):
    if (message.from_user.id in ADMIN_ID):
        bot.reply_to(message, "Bot đã tắt🪫")
        bot.stop_polling()

bot.infinity_polling()
os.system("python stop.py")
