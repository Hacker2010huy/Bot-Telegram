import telebot,os,time,requests,enc
from datetime import timedelta
from keep_alive import keep_alive
keep_alive()
print("Bot online")

bot = telebot.TeleBot("7399774608:AAExFx2rNd_LYCBfTHGDMQWpzBFs7JFFm4U", parse_mode="HTML")
file_acc = "pqhsave.json"
ADMIN_ID = [6481553299]
start_time = time.time()

#Lệnh
@bot.message_handler(commands=['start', 'help'])
def ds_lenh(message):
	text = '''
PHAN QUOC HUY BOT
=================
Danh sách các lệnh
=================
/help - Xem lệnh
/tx - Sắp có hoặc không:)
/status - Xem trạng thái bot
Tự động:
gửi file .py để enc
ADMIN:
/offbot - Tắt bot
/onbot - Bật bot
'''
	bot.reply_to(message, text);

@bot.message_handler(commands=['status'])
def status_bot(message):
    current_time = time.time()
    elapsed_time = current_time - start_time
    days, seconds = elapsed_time // 86400, elapsed_time % 86400
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    bot.send_message(message.chat.id, f"Bot đã chạy được {int(days)} ngày {int(hours)} giờ {int(minutes)} phút {int(seconds)} giây")

#Tự động
@bot.message_handler(content_types=['document'])
def get_file(message):
    user_id = message.from_user.id
    if message.document.file_name.split('.')[-1] == 'py':
        file_id = message.document.file_id
        filename = f"{user_id}_{message.document.file_name}"
        file_path = bot.get_file(file_id).file_path
        file_content = bot.download_file(file_path).decode('utf-8')
        enc.pyThon(file_content, filename)
        bot.send_document(message.chat.id, open(filename, "rb"))
        os.remove(filename)

#admin
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
