import telebot,os,time,requests
from keep_alive import keep_alive
keep_alive()
print("Bot online")

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
/tx - Sắp có rồi nha:)
ADMIN:
/offbot - Tắt bot
/onbot - Bật bot
'''
	bot.reply_to(message, text);

@bot.message_handler(commands=['offbot'])
def offbot(message):
    if (message.from_user.id in ADMIN_ID):
        text_code = requests.get("https://raw.githubusercontent.com/Hacker2010huy/Bot-Telegram/main/main.py").text
        with open("main.py", "w", encoding="utf-8") as f:
            f.write(text_code)
        bot.reply_to(message, "Bot đã tắt🪫")
        bot.stop_polling()

bot.infinity_polling()
os.system(f"python stop.py")
