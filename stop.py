import telebot,os,time,requests
from keep_alive import keep_alive
keep_alive()
print("Bot offline")

bot = telebot.TeleBot("7399774608:AAExFx2rNd_LYCBfTHGDMQWpzBFs7JFFm4U", parse_mode="HTML")
ADMIN_ID = [6481553299]

@bot.message_handler(commands=['onbot'])
def onbot(message):
    if (message.from_user.id in ADMIN_ID):
    	text_code = requests.get("https://raw.githubusercontent.com/Hacker2010huy/Bot-Telegram/main/main.py").text
    	with open("main.py", "w", encoding="utf-8") as f:
        	f.write(text_code)
        bot.reply_to(message, "Bot đã bật🔋")
        bot.stop_polling()

bot.infinity_polling()
os.system(f"python3 main.py")
