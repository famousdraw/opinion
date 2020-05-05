from app import app
from flask import render_template
from crawler import crawler
import datetime
@app.route('/')
@app.route('/index')
def index():
    today=datetime.date.today()
    news=crawler.crawler()
    year = str(today.year)
    month = str(today.month)
    day = str(today.day)
    message = '今天是' + year + '年' + month + '月' + day + '日'
    messages=[]
    messages.append(message)
    welcome_message='欢迎使用舆情监测系统！'
    messages.append(welcome_message)
    return render_template('index.html',messages=messages,title='舆情监测',news=news)