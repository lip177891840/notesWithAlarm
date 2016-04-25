#!coding=utf-8
#这个模块处理增加,修改,删除部分   对应file里的write,delete,change
import os, sys ,datetime
import random
try:
	from fileSystem.file import MyNote,MyFile
except:
	print "../file not exist"

class Alter():
	def __init__(self):
		self.myfile =MyFile()

	def writeOneMynote(self,myNote):
		self.myfile.writeNoteAndData(myNote)

	def changeOneMynote(self,myNote):
		self.myfile.changeNoteAndData(myNote)

	def deleteOneMynote(self,myNote):
		self.myfile.deleteNoteAndData(myNote)

	def writeMynoteByDate(self,date):
		myNote =MyNote()
		noteList= self.myfile.readNote()
		String1= str(date[0])+"-"+str(date[1]+1)+"-"+str(date[2])
		String2= str(random.randint(0,23))+"-"+str(random.randint(0,59))+"-"+str(random.randint(0,59))
		dateString=String1+" "+String2
		time=datetime.datetime.strptime(dateString,'%Y-%m-%d %H-%M-%S')
		print time
		#查询是否存在这个时间
		has=False
		for note in noteList:
			if date==note.time:
				has=True
		if has: #这里以后需要改进一下
			String1= str(date[0])+"-"+str(date[1]+1)+"-"+str(date[2])
			String2= str(random.randint(0,23))+"-"+str(random.randint(0,59))+"-"+str(random.randint(0,59))
			dateString=String1+" "+String2
			time=datetime.datetime.strptime(dateString,'%Y-%m-%d %H-%M-%S')

		myNote.time=time
		myNote.title=String1
		self.myfile.writeNoteAndData(myNote)
		return myNote




if __name__ =="__main__":
	a=Alter()
	f=MyFile()
	myNoteList=f.readNoteAndData()
	myNoteList[1].title="firefox"
	print os.getcwd()
	a.deleteOneNote(myNoteList[4])