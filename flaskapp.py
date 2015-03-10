import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

import smtplib
from email.mime.text import MIMEText  

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

sourc_mail_addr = "cexuscastle@126.com"
dest_mail_addr = ["cexuscastle@126.com"]

def sendWarningMail (text):  
    msg = MIMEText(text)  
    msg['Subject'] = "It's from OpenShift"  
    msg['From'] = sourc_mail_addr  
    smtp = smtplib.SMTP()  
    smtp.connect(r'smtp.126.com')
    smtp.login(sourc_mail_addr, "zxcvbnm123")  
    smtp.sendmail(sourc_mail_addr, dest_mail_addr, msg.as_string())  
    smtp.close()

@app.route('/')
@app.route('/index')
def index():
    sendWarningMail("It's from OpenShift for Castle!!!")
    return "<strong>Hello, Maomaosong!!!</strong>"

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

if __name__ == '__main__':
    app.run()
