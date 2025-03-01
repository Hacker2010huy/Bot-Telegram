import telebot,os,time,requests
from keep_alive import keep_alive
keep_alive()

bot = telebot.TeleBot("7399774608:AAExFx2rNd_LYCBfTHGDMQWpzBFs7JFFm4U", parse_mode="HTML")
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

pip_text = requests.get("https://raw.githubusercontent.com/Hacker2010huy/Bot-Telegram/main/requirements.txt").text.replace("\n", " ")
os.system(f"pip install {pip_text}")
print("bot offed")
text_code = requests.get("https://raw.githubusercontent.com/Hacker2010huy/Bot-Telegram/main/main.py").text.replace("\n", "; ")
os.system(f"python -c {text_code}")
