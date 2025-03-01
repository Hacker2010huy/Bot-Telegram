from keep_alive import keep_alive
keep_alive()

import telebot,os,time
bot = telebot.TeleBot("7399774608:AAExFx2rNd_LYCBfTHGDMQWpzBFs7JFFm4U", parse_mode="HTML")
ADMIN_ID = [6481553299]

@bot.message_handler(commands=['onbot'])
def offbot(message):
    if (message.from_user.id in ADMIN_ID):
        bot.reply_to(message, "Bot đã bật🔋")
        bot.stop_polling()

bot.infinity_polling()

pip_text = requests.get("https://raw.githubusercontent.com/Hacker2010huy/Bot-Telegram/main/requirements.txt").text.replace("\n", " ")
os.system(f"pip install {pip_text}")
text_code = requests.get("https://raw.githubusercontent.com/Hacker2010huy/Bot-Telegram/main/main.py").text
with open("main.py", "w", encoding="utf-8") as f:
	f.write(text_code)
os.system(f"python main.py")
