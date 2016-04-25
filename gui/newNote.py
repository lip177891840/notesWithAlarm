#coding:utf-8
#这是new菜单项窗口的类
import gtk
import sys,os,time,datetime
sys.path.append('..')



class NewNote(gtk.Window):
	havaSave =False
	def __init__(self):
		#import some
		try:
			from control.getNotes import Get
			from control.alterNotes import Alter
			from fileSystem.file import MyNote
		except:
			print "import error(gui/nowNote)"
			sys.exit()
			
		self.myNote =MyNote()
		self.get =Get()
		self.alter =Alter()

		super(NewNote,self).__init__()
		#self.connect("destroy",gtk.main_quit)
		self.set_title("new note")
		self.set_size_request(390,290)
		self.set_position(gtk.WIN_POS_CENTER)

		self.create_toolbar()
		self.create_setting()
		self.create_textview()
		vbox = gtk.VBox(False, 0)
		vbox.pack_start(self.toolbar, False, False, 0)
		vbox.pack_start(self.notebook,False,False,0)
		vbox.pack_start(self.scrolledWindow,True, True, 0)
		
		self.add(vbox)
		self.connect("key_press_event",self.on_key_press_event)

		self.show_all()
		#----------hide some widgets firstly----------
		self.notebook.hide()
		self.time_label4.hide()
		self.spinButton4.hide()
		self.time_button_minute_show.set_active(True)

	def create_toolbar(self):
		self.toolbar =gtk.Toolbar()
		list =gtk.stock_list_ids()

		self.check_button =gtk.CheckButton()
		self.string="test"
		#----open save clear bold italic spell-------------
		opentb =gtk.ToolButton(gtk.STOCK_OPEN)
		opentb.set_tooltip_text("Open(Ctrl-o)")
		opentb.connect("clicked",self.open_new_note,self.string)

		savetb =gtk.ToolButton(gtk.STOCK_SAVE)
		savetb.set_tooltip_text("Save(Ctrl-s)")
		savetb.connect("clicked",self.save_note)

		cleartb =gtk.ToolButton(gtk.STOCK_CLEAR)
		cleartb.set_tooltip_text("Clear")
		cleartb.connect("clicked",self.clear_text)

		boldtb =gtk.ToolButton(gtk.STOCK_BOLD)
		boldtb.set_tooltip_text("Bold")
		boldtb.connect("clicked",self.bold_clicked,self.string)

		italictb =gtk.ToolButton(gtk.STOCK_ITALIC)
		italictb.set_tooltip_text("Italic")
		italictb.connect("clicked",self.italic_clicked,self.string)

		spell_cheek =gtk.ToolButton(gtk.STOCK_SPELL_CHECK)
		spell_cheek.set_tooltip_text("Spell_check")
		spell_cheek.connect("clicked",self.spell_clicked)

		sep = gtk.SeparatorToolItem()
		#---------setting isOn importance quit---------------
		settingtb =gtk.ToggleToolButton(list[31])
		settingtb.set_tooltip_text("Setting")
		settingtb.connect("clicked",self.setting)

		self.isOn =gtk.ToggleToolButton(list[70])
		self.isOn.set_tooltip_text("On/Off")
		self.isOn.connect("toggled",self.set_isOn,self.check_button)

		importance =gtk.ToggleToolButton(gtk.STOCK_SORT_ASCENDING)
		importance.set_tooltip_text("Importance")
		#importance.connect("toggled",self.set_inportance,self.string)

		quittb = gtk.ToolButton(gtk.STOCK_CLOSE)
		quittb.set_tooltip_text("Quit")
		#quittb.connect("clicked",self.on_button_clicked,self.string)

		self.toolbar.insert(opentb, 0)
		self.toolbar.insert(savetb, 1)
		self.toolbar.insert(cleartb,2)
		
		self.toolbar.insert(boldtb, 3)
		self.toolbar.insert(italictb, 4)
		self.toolbar.insert(spell_cheek, 5)

		self.toolbar.insert(sep, 6)
		self.toolbar.insert(settingtb,7)
		self.toolbar.insert(self.isOn,8)
		self.toolbar.insert(importance,9)
		self.toolbar.insert(quittb, 10)

	# note's setting ---------hide firstly---------
	def create_setting(self):
		self.show=False #show or hide this setting
		self.notebook =gtk.Notebook()
		#------title------------
		title_frame =gtk.Frame()
		title_hbox =gtk.HBox()
		self.title_entry =gtk.Entry()
		title_button_ok =gtk.Button("Ok")
		title_button_ok.connect("clicked",self.titleSetting)
		title_hbox.add(self.title_entry)
		title_hbox.add(title_button_ok)
		title_frame.add(title_hbox)
		self.notebook.append_page(title_frame,gtk.Label("Title"))
		#-------AlarmTime-------------
		self.hasAlarmTime =False
		time_frame =gtk.Frame()
		time_hbox =gtk.HBox()
		time_label1=gtk.Label("M:")
		time_adjustment1 =gtk.Adjustment(1.0, 1.0, 12.0, 1.0, 5.0, 0.0)
		spinButton1 =gtk.SpinButton(time_adjustment1,1,0)

		time_label2 =gtk.Label("D")
		time_adjustment2 =gtk.Adjustment(1.0, 1.0, 31.0, 1.0, 5.0, 0.0)
		spinButton2 =gtk.SpinButton(time_adjustment2,1,0)

		time_label3 =gtk.Label("H")
		time_adjustment3 =gtk.Adjustment(0.0, 0.0, 24.0, 1.0, 5.0, 0.0)
		spinButton3 =gtk.SpinButton(time_adjustment3,1,0)

		self.time_label4 =gtk.Label("Min")
		time_adjustment4 =gtk.Adjustment(0.0, 0.0, 60.0, 1.0, 5.0, 0.0)
		self.spinButton4 =gtk.SpinButton(time_adjustment4,1,0)
		self.time_button_minute_show =gtk.ToggleButton("Min")
		self.time_button_minute_show.connect("toggled",self.minute_button,self.time_label4,self.spinButton4)
		time_button_add=gtk.Button("Add")
		time_button_add.connect("clicked",self.time_button_add,spinButton1,spinButton2,spinButton3,self.spinButton4)

		time_hbox.add(time_label1)
		time_hbox.add(spinButton1)
		time_hbox.add(time_label2)
		time_hbox.add(spinButton2)
		time_hbox.add(time_label3)
		time_hbox.add(spinButton3)
		time_hbox.add(self.time_label4)
		time_hbox.add(self.spinButton4)
		time_hbox.add(self.time_button_minute_show)
		time_hbox.add(time_button_add)
		time_frame.add(time_hbox)
		self.notebook.append_page(time_frame,gtk.Label("Alarm"))

		isOn_frame =gtk.Frame()
		isOn_hbox =gtk.HBox()
		isOn_hbox.add(gtk.Label("Turn on/off this Alarm"))
		
		self.check_button.connect("toggled",self.set_isOn,self.isOn)
		isOn_hbox.add(self.check_button)
		isOn_frame.add(isOn_hbox)
		self.notebook.append_page(isOn_frame,gtk.Label("IsOn"))

		#------------importance--------------
		importance_frame =gtk.Frame()
		importance_hbox =gtk.HBox()
		importance_hbox.add(gtk.Label("Set importance of this note"))

		radio_button1=gtk.RadioButton(None,"1")
		radio_button1.connect("toggled",self.radio_button_clicked,"1")
		importance_hbox.add(radio_button1)

		radio_button2 =gtk.RadioButton(radio_button1,"2")
		radio_button2.connect("toggled",self.radio_button_clicked,"2")
		importance_hbox.add(radio_button2)

		radio_button3 =gtk.RadioButton(radio_button1,"3")
		radio_button3.connect("toggled",self.radio_button_clicked,"3")
		importance_hbox.add(radio_button3)
		importance_frame.add(importance_hbox)
		self.notebook.append_page(importance_frame,gtk.Label("Importance"))

	def create_textview(self):
		self.scrolledWindow =gtk.ScrolledWindow()
		self.textview =gtk.TextView()
		self.textbuffer =self.textview.get_buffer()
		self.textbuffer.set_text("this is a test")
		self.scrolledWindow.add(self.textview)
	#--------------open save clear--------------
	def open_new_note(self,widget,string):
		#gtk.main_quit()
		AllNotes()
		#get= Get()
		#myNoteList = get.getAllNotes()
		#print myNoteList

	def save_note(self,widget):
		#在被调用时,要把self.myNote的各个属性得到
		#--time---
		currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
		now=datetime.datetime.strptime(currentTime,'%Y-%m-%d %H:%M:%S')
		self.myNote.time=now
		#--title---
		self.titleSetting(widget)
		#--alarm---
		#--isOn--importance---(这两个已经设置)---
		#--data------
		start,end =self.textbuffer.get_bounds()
		data=self.textbuffer.get_text(start,end)
		self.myNote.data=data
		#判断是否保存
		if self.havaSave:
			print "hava saved"
		else:
			self.alter.writeOneMynote(self.myNote)
			print "going to save note"
			self.havaSave=True
			print self.myNote.time
			print self.myNote.title
			print self.myNote.alarm
			print self.myNote.isOn
			print self.myNote.importance
			print self.myNote.data

	def clear_text(self,widget):
		self.textbuffer.set_text("")

	#-------------bold italic spell -----------------
	def bold_clicked(self, widget,string):
		pass
	def italic_clicked(self,widget,string):
		pass
	def spell_clicked(self,widget):
		pass
	#------------===Setting===  --title time  isOn importance  -------------
	def setting(self,widget): #笔记的设置显示和隐藏
		if self.show:
			self.notebook.hide()
			self.show =False
		else:
			self.notebook.show()
			self.show=True

	def titleSetting(self,widget):
		title=self.title_entry.get_text()
		if title.count("#") ==0 and len(title) !=0:
			self.myNote.title=title

	def minute_button(self,widget,arg1,arg2): #分钟设置的显示和隐藏
		if widget.get_active:
			arg1.hide()
			arg2.hide()
		if not widget.get_active():
			arg1.show()
			arg2.show()

	def time_button_add(self,widget,spin1,spin2,spin3,spin4):
		year=time.strftime('%Y',time.localtime())
		month =spin1.get_value_as_int()
		day =spin2.get_value_as_int()
		hour =spin3.get_value_as_int()
		minute =spin4.get_value_as_int()
		alarm_timeString =year+"-"+str(month)+"-"+str(day)+" "+str(hour)+":"+str(minute)+":00"
		if alarm_timeString != year+"-1-1 0:0:00":
			alarm_time=datetime.datetime.strptime(alarm_timeString,'%Y-%m-%d %H:%M:%S')
			spin1.set_value(1)
			spin2.set_value(1)
			spin3.set_value(0)
			spin4.set_value(0)
			if self.myNote.alarm.count(alarm_time) ==0:
				self.myNote.alarm.append(alarm_time)
			print self.myNote.alarm



	def radio_button_clicked(self,widget,data=None):  #importance setting
		if data =="1":
			self.myNote.importance=1
		elif data =="2":
			self.myNote.importance=2
		elif data =="3":
			self.myNote.importance=3
		else:
			print "error"

	#-------------end of setting------------------
	def set_isOn(self,toolButton,check_button):
		#there is a mistake between toolButton and check_button when called by self.check_button and self.isOn,
		#but it also works.Called by self_isOn,order of arguments is right,but wrong called by self.check_button.
		#这里有个小错误,但也能达到相同的功能,当被self.isOn调用时参数是正确的,而被self.chekc_button调用时是相反的
		if toolButton.get_active()==True and check_button.get_active()==False and self.myNote.isOn==0:
			self.myNote.isOn=1
			check_button.set_active(True)
			#print "1"
		elif toolButton.get_active()==True and check_button.get_active()==False and self.myNote.isOn==1:
			self.myNote.isOn=0
			toolButton.set_active(False)
			#print "2"
		elif toolButton.get_active()==False and check_button.get_active()==True and self.myNote.isOn==0:
			self.myNote.isOn=1
			toolButton.set_active(True)
			#print "3"
		elif toolButton.get_active()==False and check_button.get_active()==True and self.myNote.isOn==1:
			self.myNote.isOn=0
			check_button.set_active(False)
			#print "4"

	def on_key_press_event(self,widget, event):
		from gtk.gdk import CONTROL_MASK
		keyname =gtk.gdk.keyval_name(event.keyval)
		if event.state & CONTROL_MASK:
			if keyname == "s":
				self.save_note(widget)
			elif keyname == "o":
				self.open_new_note(widget,self.string)
			elif keyname == "q":
				print "im going to quit"

if __name__ == "__main__":
	NewNote()
	gtk.main()
