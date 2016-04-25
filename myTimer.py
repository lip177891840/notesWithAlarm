#!coding=utf-8
import sys, os, gtk
import datetime,time
import threading
sys.path.append('..')


from fileSystem.file import MyNote,MyFile
from gui.alarm import Alarm

#把Alarm(闹钟提醒窗口)放在线程中
class RunAlarm(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		self.alarm=Alarm()
		gtk.main()

class MyTimer():
	def __init__(self):
		self.f =MyFile()
		self.update_alarmList()
		
	def update_alarmList(self):
		myNoteList =self.f.readNote()
		self.alarmList_by_note=[]
		for myNote in myNoteList:
			self.alarmList_by_note.append(myNote.alarm)

	def main_loop(self):
		while True:
			#更新self.alarmList_by_note
			self.update_alarmList()
			nextTime =self.get_next_time()
			if nextTime>10:
				print "sleep %s s" %str(nextTime-10)
				time.sleep(nextTime-10)
				print "createWindow after 10 s"
				timer =threading.Timer(10,self.createWindow)
				timer.start()
			else:
				print "createWindow after %s s" %nextTime
				timer =threading.Timer(nextTime,self.createWindow)
				timer.start()
			exit()

	def createWindow(self):
		print "creating window"
		#gtk.gdk.threads_init()
		#runAlarm=RunAlarm()
		#runAlarm.start()

	def get_next_time(self): #获得下一个最近的时间,返回的是秒数
		nowString=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
		print nowString
		now=datetime.datetime.strptime(nowString,'%Y-%m-%d %H:%M:%S')
		a=datetime.datetime.strptime('2015-01-01 00:00:00','%Y-%m-%d %H:%M:%S')
		b=datetime.datetime.strptime('2015-01-02 00:00:00','%Y-%m-%d %H:%M:%S')
		minTime =b-a #默认最小时间是一天的时间
		for i in range(len(self.alarmList_by_note)):
			for alarm in self.alarmList_by_note[i]:
				if alarm >now:
					if alarm -now <minTime:
						minTime= alarm-now
		print minTime
		#minTime.seconds 是把时间差转换为秒数
		#print minTime.seconds
		#return minTime.seconds
		return 11

if __name__ == "__main__":
	myTimer=MyTimer()
	try:
		myTimer.main_loop()
	except (KeyboardInterrupt, SystemExit):
		print "Bye"