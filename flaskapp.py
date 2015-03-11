import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

import urllib2
import thread
from threading import Timer
import smtplib,re  
from email.mime.text import MIMEText  

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
@app.route('/index')
def index():
    return "<strong>Hello, Maomaosong!!!</strong>"

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

def canSendMailAgain():
    print "Timer handler"
    
sourc_mail_addr = "cexuscastle@126.com"
dest_mail_addr = ["cexuscastle@126.com"]

def sendWarningMail (text):  
    msg = MIMEText(text)  
    msg['Subject'] = "Aptamil 1+ comming!!!"  
    msg['From'] = sourc_mail_addr  
    smtp = smtplib.SMTP()  
    smtp.connect(r'smtp.126.com')
    smtp.login(sourc_mail_addr, "zxcvbnm123")  
    smtp.sendmail(sourc_mail_addr, dest_mail_addr, msg.as_string())  
    smtp.close() 
    
if __name__ == '__main__':
    app.debug = True
    #TIMERRUNNING = Timer(2.0, canSendMailAgain, [])
    #TIMERRUNNING.start()
    #f = urllib2.urlopen('http://www.python.org/')
    #print f.read(100)
    sendWarningMail("hahaha")
    app.run()

    

