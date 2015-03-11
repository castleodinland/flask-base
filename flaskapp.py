import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

import urllib2
import thread
from threading import Timer

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
@app.route('/index')
def index():

    return "<strong>Hello, world!</strong>"
@app.route("/test")
def test():
    f = urllib2.urlopen('http://www.windeln.de/zh/aptamil-milchnahrung.html?selectedean=4008976022299')
    return "%s" %(f.read())

def canSendMailAgain():
    print "Timer handler"
    
if __name__ == '__main__':
    app.debug = True
    #TIMERRUNNING = Timer(2.0, canSendMailAgain, [])
    #TIMERRUNNING.start()
    app.run()

    

