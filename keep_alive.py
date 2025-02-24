from flask import Flask,render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot alive"

def run():
    app.run(host='0.0.0.0', port=8000)
    t = Thread(target=run)
    t.start()
