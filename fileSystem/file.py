#!coding=utf-8
import os, sys
import datetime,time
#不是工作在当前路径下
notesFile="fileSystem/notes.txt"
dataFileDir="fileSystem/data/"
#notesFile="notes.txt"
#dataFileDir="data/"

class MyNote():
	currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

	def __init__(self,time=currentTime,title=currentTime,alarm='[]',isOn=0,importance=1,data=""):
		self.time=datetime.datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
		self.title=title
		self.alarm=[]
		if alarm !='[]':
			for i in alarm.strip('[]').split(","):
				self.alarm.append(datetime.datetime.strptime(i,'%Y-%m-%d %H:%M:%S'))
		self.isOn=int(isOn)
		self.importance=int(importance)

		self.data=""

# this is a class to read/write file,provide functions to up layer
class MyFile():
	#some properties of the class
	#myNote类型包括note部分和data部分
	def __init__(self):
		#os.chdir("../fileSystem")
		print os.getcwd()
		#pass

	#--------------------Note-------------------------
	def readNote(self): #从文件(notes.txt)中读取数据,返回一个MyNote对象列表
		#先从notes.txt中读取数据,得到一个note字符串的列表noteString_list
		try:
			notes_file=open(notesFile)
		except:
			print "readNote failed(fileSystem/file)"
			sys.exit()
		noteString_list=notes_file.readlines()
		noteString_list=noteString_list[1:len(noteString_list)]
		#把该字符串列表中的每个字符串解析并封装到MyNote对象里,然后添加该对象到noteList
		noteList=[]
		for noteString in noteString_list:
			noteList.append(self.stringToMyNote(noteString))
		notes_file.close()
		return noteList

	def writeNote(self,myNote): #在最后增加一个note,参数是一个myNote
		try:
			notes_file=open(notesFile,"a")
		except:
			print "writeNote failed(fileSystem/file)"
		string =self.MyNoteToString(myNote)
		try:
			notes_file.write(string)
		except:
			print "writeNote failed failed(fileSystem/file)"
		notes_file.close()

	def deleteNote(self,myNote): #删除一个note,参数是一个myNote
		myNoteList =self.readNote()
		index=-1
		for i in myNoteList:
			if i.time == myNote.time:
				index=myNoteList.index(i)
		if index == -1:
			return False
		else:
			myNoteList.remove(myNoteList[index])
			try:
				notes_file=open(notesFile,"w")
				notes_file.write("#time     #标题  #提醒时间  #是否开启 #重要级")
			except:
				print "deleteNote failed(fileSystem/file)"
			for myNote in myNoteList:
				string =self.MyNoteToString(myNote)
				notes_file.write(string)
			notes_file.close()
			return True

	def changeNote(self,myNote): #修改一个note,参数是一个myNote
		myNoteList =self.readNote()
		index=-1
		for i in myNoteList:
			if i.time == myNote.time:
				index=myNoteList.index(i)
		if index == -1:
			return False
		else:
			myNoteList.remove(myNoteList[index])
			myNoteList.insert(index,myNote)
			try:
				notes_file=open(notesFile,"w")
				notes_file.write("#time     #标题  #提醒时间  #是否开启 #重要级")
			except:
				print "changeNote failed(fileSystem/file)"
			for myNote in myNoteList:
				string =self.MyNoteToString(myNote)
				notes_file.write(string)
			notes_file.close()
			return True

	#-----------------------Data------------------
	def readData(self,time):#从文件(data/time)读取数据,返回一个字符串列表
		time=time.strftime('%Y-%m-%d %H:%M:%S')
		try:
			data_file= open(dataFileDir+time)
			data =data_file.readlines()
		except:
			print "readData failed(fileSystem/file)"
			sys.exit()
			
		string=""
		if len(data)==0:
			return ""
		else:
			for i in range(len(data)):
				string=string+data[i]
			return string

	def writeData(self,time,data):
		time=time.strftime('%Y-%m-%d %H:%M:%S')
		try:
			data_file= open(dataFileDir+time,'w')
			data_file.write(data)
		except:
			print "writeData failed(fileSystem/file)"

	def deleteData(self,time):
		time=time.strftime('%Y-%m-%d %H:%M:%S')
		if os.path.exists(dataFileDir+time):
			os.remove(dataFileDir+time)
		else:
			print "deleteData failed(fileSystem/file)"

	def changeData(self,time,data):
		time=time.strftime('%Y-%m-%d %H:%M:%S')
		try:
			data_file= open(dataFileDir+time,'w')
			data_file.write(data)
		except:
			print "changeData failed(fileSystem/file)"
	#-----------------------Note + Data---------
	def readNoteAndData(self):
		myNoteList=self.readNote()
		for i in range(len(myNoteList)):
			myNoteList[i].data=self.readData(myNoteList[i].time)
		return myNoteList

	def writeNoteAndData(self,myNote):
		self.writeNote(myNote)
		self.writeData(myNote.time,myNote.data)

	def deleteNoteAndData(self,myNote):
		self.deleteNote(myNote)
		self.deleteData(myNote.time)

	def changeNoteAndData(self,myNote):
		self.changeNote(myNote)
		self.changeData(myNote.time,myNote.data)
	#-----------------------some util------------------
	def stringToMyNote(self,string):
		string=string.strip('\n')
		list=string.split('#')
		return MyNote(list[0],list[1],list[2],list[3],list[4])
	
	def MyNoteToString(self,myNote):
		time=myNote.time.strftime('%Y-%m-%d %H:%M:%S')
		title=myNote.title
		#----alarm------
		s="["
		if len(myNote.alarm) !=0:
			for i in myNote.alarm:
				s=s+i.strftime('%Y-%m-%d %H:%M:%S')+","
			s=s[0:len(s)-1]+"]"
		else:
			s="[]"
		isOn=str(myNote.isOn)
		importance=str(myNote.importance)
		string="\n"+time+"#"+title+"#"+s+"#"+isOn+"#"+importance

		return string



if __name__ == "__main__":
	f=MyFile()
	myNoteList=f.readNote()
	print len(myNoteList)
	data =f.readData(myNoteList[8].time)
	print data
	#f.deleteNoteAndData(myNoteList[0])
	#print myNoteList[2].data
