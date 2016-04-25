#!coding=utf-8
#这个模块用来处理查询相关的部分,对应file模块里的read
import sys, os
import datetime,time
sys.path.append('..')

try:
	from fileSystem.file import MyNote,MyFile
except:
	print "../file not exist(control/getNotes)"

class Get():
	def __init__(self):
		pass

	def getAllNotes(self):
		f=MyFile()
		#print os.getcwd()
		myNoteList=f.readNoteAndData()
		return myNoteList

	def getOneNote(self,time):
		for myNote in self.myNoteList_by_day:
			if time == myNote.time:
				return myNote

	def getSomeNotes_by_day(self,date): #date example:(2015,11,26)
		myNoteList_by_day=[]
		myNoteList =self.getAllNotes()

		tmpString= str(date[0])+str(date[1])+str(date[2])
		date_of_day =datetime.datetime.strptime(tmpString,'%Y%m%d')
		#print date_of_day
		dateString =date_of_day.strftime('%Y-%m-%d')
		#print dateString

		for myNote in myNoteList:
			if myNote.time.strftime('%Y-%m-%d') == dateString:
				myNoteList_by_day.append(myNote)
		self.myNoteList_by_day =myNoteList_by_day
		return myNoteList_by_day

if __name__ == "__main__":
	get= Get()
	#print get.getAllNotes()[0].time #== "2015-11-17 14:34:00"
	print len(get.getSomeNotes_by_day((2015,11,26)))