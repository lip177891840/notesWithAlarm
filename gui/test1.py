#!coding=utf-8
import sys, os, gtk
import datetime,time
import threading
try:
    from test import Alarm
    from test2 import Win
except:
    print "../file not exist"
#把Alarm(闹钟提醒窗口)放在线程中
class RunAlarm(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        #print "1"
        alarm=Alarm()

class RunAlarm1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        #print "1"
        win=Win()

class MyTimer():
    def main_loop(self):

        timer =threading.Timer(3,self.createWindow)
        timer1 =threading.Timer(5,self.createWindow1)
        timer.start()
        timer1.start()
        time.sleep(6)


    def createWindow(self):
        gtk.gdk.threads_init()
        runAlarm=RunAlarm()
        runAlarm.start()

    def createWindow1(self):
        gtk.gdk.threads_init()
        runAlarm1=RunAlarm1()
        runAlarm1.start()

if __name__ == "__main__":
    myTimer=MyTimer()
    try:
        myTimer.main_loop()
    except (KeyboardInterrupt, SystemExit):
        print "Bye"