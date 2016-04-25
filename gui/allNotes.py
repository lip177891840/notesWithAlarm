#coding:utf-8
#主窗口
import gtk
import sys,os,time,datetime
sys.path.append('..')
from gui.about import About
from control.getNotes import Get#好郁闷为什么这行不能放在__init__里

class AllNotes(gtk.Window):
	def __init__(self):
		#import some
		try:
			
			from control.alterNotes import Alter
			from fileSystem.file import MyNote
		except:
			print "import error(gui/allNote)"
			sys.exit()

		self.alter=Alter()
		self.myNote=MyNote()
		#import some
		super(AllNotes,self).__init__()
		#self.connect("destroy",gtk.main_quit)
		self.set_title("None")
		self.set_size_request(750,510)
		self.set_position(gtk.WIN_POS_CENTER)
		
		self.set_icon_from_file("images/2.png")

		table =gtk.Table(13,5,True)
		#-------calendar----------
		frame1=self.create_calendar()
		table.attach(frame1,0,1,0,5)
		#每一天的所有notes
		frame2=self.create_notes_list()
		table.attach(frame2,0,1,5,12)
		#boolbar 35 pixel
		toolBar=self.create_toolbar()
		table.attach(toolBar,1,5,0,1)
		#editor
		textviewEdit=self.create_editor()
		table.attach(textviewEdit,1,4,1,13)
		#note's setting
		setting_frame=self.create_setting()
		table.attach(setting_frame,4,5,1,13)

		self.add(table)
		self.show_all()
		#默认隐藏一些东西
		self.alarm_label.hide()
		self.alarm_entry.hide()
		self.tmp_hbox.hide()
		self.alarm_format_label.hide()

	#=======  calendar  ========
	def create_calendar(self):
		frame1 =gtk.Frame("Calendar")
		self.calendar =gtk.Calendar()
		self.calendar.connect("month_changed", self.calendar_month_changed)
		self.calendar.connect("day_selected", self.calendar_day_selected)
		self.calendar.connect("day_selected_double_click",self.calendar_day_selected_double_click)
		frame1.add(self.calendar)
		self.today=self.calendar.get_date()
		return frame1

	def calendar_month_changed(self,widget):
		pass

	def calendar_day_selected(self,widget):
		tmp_date =self.calendar.get_date()
		date =tmp_date[0],tmp_date[1]+1,tmp_date[2]
		get =Get()
		myNoteList_by_day =get.getSomeNotes_by_day(date)
		self.myNoteList_by_day =myNoteList_by_day
		#print get.getOneNote(myNoteList_by_day[0].time).title
		self.noteListstore.clear()
		if len(myNoteList_by_day) !=0:
			for i in range(len(myNoteList_by_day)):
				self.noteListstore.append([myNoteList_by_day[i].title])

	def calendar_day_selected_double_click(self,widget):
		#双击日历上的日期,新建这天的myNote
		print "double_click"
		date =self.calendar.get_date()
		self.myNote=self.alter.writeMynoteByDate(date)
		#刷新notes_list
		self.calendar_day_selected(widget)
		self.change_editor()
		self.change_setting()
		self.set_title(self.myNote.title)

	#========  notes_list  =====
	def create_notes_list(self):
		frame2 =gtk.Frame("Day's notes")
		scrolledWindow =gtk.ScrolledWindow()
		self.noteListstore =gtk.ListStore(str)
		#先得到当天日期(初始化)
		self.calendar_day_selected(self.calendar)

		treeview =gtk.TreeView(self.noteListstore)
		treeview.connect('row-activated',self.oneNote_clicked)
		tvcolumn=gtk.TreeViewColumn('title')
		cell=gtk.CellRendererText()
		tvcolumn.pack_start(cell,True)
		tvcolumn.add_attribute(cell,'text',0)
		treeview.append_column(tvcolumn)
		scrolledWindow.add(treeview)
		frame2.add(scrolledWindow)
		return frame2

	def oneNote_clicked(self,treeview,path,column):
		self.myNote =self.myNoteList_by_day[path[0]]
		self.set_title(self.myNote.title)

		self.change_editor()
		self.change_setting()

	#========  toolbar  ========
	def create_toolbar(self):
		toolBar =gtk.Toolbar()
		hometb =gtk.ToolButton(gtk.STOCK_HOME)
		hometb.set_tooltip_text("Today")
		hometb.connect("clicked",self.hometb_clicked)
		
		savetb =gtk.ToolButton(gtk.STOCK_SAVE)
		savetb.set_tooltip_text("Save")
		savetb.connect("clicked",self.savetb_clicked)
		deletetb =gtk.ToolButton(gtk.STOCK_DELETE)
		deletetb.set_tooltip_text("DeleteCurrentNote")
		deletetb.connect("clicked",self.deletetb_clicked)
		cleartb =gtk.ToolButton(gtk.STOCK_CLEAR)
		cleartb.set_tooltip_text("Clear")
		cleartb.connect("clicked",self.cleartb_clicked)

		boldtb =gtk.ToolButton(gtk.STOCK_BOLD)
		boldtb.set_tooltip_text("Bold")
		italictb =gtk.ToolButton(gtk.STOCK_ITALIC)
		italictb.set_tooltip_text("Italic")
		spell_cheek =gtk.ToolButton(gtk.STOCK_SPELL_CHECK)
		spell_cheek.set_tooltip_text("SpellCheck")
		sep = gtk.SeparatorToolItem()
		quittb = gtk.ToolButton(gtk.STOCK_CLOSE)
		quittb.set_tooltip_text("Quit")
		i=1
		toolBar.insert(hometb,0)
		toolBar.insert(savetb,i+0)
		toolBar.insert(deletetb, i+1)
		toolBar.insert(cleartb,i+2)
		
		toolBar.insert(boldtb, i+3)
		toolBar.insert(italictb, i+4)
		toolBar.insert(spell_cheek, i+5)

		toolBar.insert(sep, i+6)
		toolBar.insert(quittb,i+7)
		return toolBar

	def hometb_clicked(self,widget):
		now=time.strftime('%Y-%m-%d',time.localtime())
		self.calendar.select_month(self.today[1],self.today[0])
		self.calendar.select_day(self.today[2])

	def deletetb_clicked(self,widget):
		self.alter.deleteOneMynote(self.myNote)
		#刷新notes_list
		self.calendar_day_selected(widget)

	def savetb_clicked(self,widget):
		currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
		now=datetime.datetime.strptime(currentTime,'%Y-%m-%d %H:%M:%S')
		#self.myNote.time=now
		self.myNote.title=self.title_entry.get_text()
		#alarm
		start,end =self.textBufferEdit.get_bounds()
		data=self.textBufferEdit.get_text(start,end)
		self.myNote.data=data

		print self.myNote.title
		print self.myNote.time
		print self.myNote.isOn
		print self.myNote.importance
		print self.myNote.data

		self.alter.changeOneMynote(self.myNote)

	def cleartb_clicked(self,widget):
		self.textBufferEdit.set_text("")
	def boldtb_clicked(self,widget):
		pass
	def italictb_clicked(self,widget):
		pass
	def spell_check_clicked(self,widget):
		pass
	def quittb_clicked(self,widget):
		pass
		
	#========  editor  =======
	def create_editor(self):
		textviewEdit =gtk.TextView()
		self.textBufferEdit =textviewEdit.get_buffer()
		self.textBufferEdit.set_text("center")
		return textviewEdit

	def change_editor(self):
		self.textBufferEdit.set_text(self.myNote.data)

	#========  setting  =======
	def create_setting(self):
		setting_frame =gtk.Frame("Setting")
		notebook =gtk.Notebook()
		#title
		title_frame =gtk.Frame("title")
		title_table =gtk.Table(10,1,True)
		self.title_entry =gtk.Entry()
		self.title_entry.set_width_chars(17)
		title_table.attach(self.title_entry,0,1,0,1)
		title_hbox =gtk.HBox()
		title_button_ok =gtk.Button("ok")
		title_button_ok.connect("clicked",self.title_button_ok_clicked)
		title_hbox.pack_start(title_button_ok,True,True,41)
		title_table.attach(title_hbox,0,1,1,2)
		title_frame.add(title_table)
		notebook.append_page(title_frame,gtk.Label("T"))
		#alarm
		alarm_frame =gtk.Frame("alarm")
		alarm_table =gtk.Table(10,1,True)
		scrolledWindow =self.create_alarm_list()
		alarm_table.attach(scrolledWindow,0,1,0,4)
		alarm_hbox =gtk.HBox()
		self.alarm_button_new =gtk.ToggleButton("new")
		self.alarm_button_new.connect("clicked",self.alarm_button_new_clicked)
		alarm_button_delete =gtk.Button("delete")
		alarm_button_delete.connect("clicked",self.alarm_button_delete_clicked)
		alarm_table.attach(alarm_hbox,0,1,4,5)
		alarm_hbox.pack_start(self.alarm_button_new,True,True,5)
		alarm_hbox.pack_start(alarm_button_delete,True,True,5)
		#隐藏的新增alarm部件
		self.alarm_label=gtk.Label("Format:  y-m-d h:m:s")
		self.alarm_entry=gtk.Entry()
		self.alarm_entry.set_width_chars(17)
		self.tmp_hbox=gtk.HBox()
		alarm_button_add=gtk.Button("Add")
		alarm_button_add.connect("clicked",self.alarm_button_add_clicked)
		self.tmp_hbox.pack_start(alarm_button_add,True,True,41)
		alarm_table.attach(self.alarm_label,0,1,6,7)
		alarm_table.attach(self.alarm_entry,0,1,7,8)
		alarm_table.attach(self.tmp_hbox,0,1,8,9)
		self.alarm_format_label=gtk.Label("match the format")
		alarm_table.attach(self.alarm_format_label,0,1,9,10)

		alarm_frame.add(alarm_table)
		notebook.append_page(alarm_frame,gtk.Label("A"))
		#isOs
		isOn_frame =gtk.Frame("isOn")
		isOn_table =gtk.Table(5,1,True)
		isOn_hbox =gtk.HBox()
		self.isOn_check_button =gtk.CheckButton()
		self.isOn_check_button.connect("toggled",self.isOn_check_button_clicked)
		isOn_hbox.add(gtk.Label("switch:"))
		isOn_hbox.add(self.isOn_check_button)
		isOn_table.attach(gtk.Label("turn on/off this alarm"),0,1,0,1)
		isOn_table.attach(isOn_hbox,0,1,1,2)
		isOn_frame.add(isOn_table)
		notebook.append_page(isOn_frame,gtk.Label("is"))
		#importance
		importance_frame =gtk.Frame("importance")
		importance_table =gtk.Table(5,1,True)
		importance_table.attach(gtk.Label("Set importance of this \nnote,and  3 is very \nimportant"),0,1,0,1)

		importance_hbox =gtk.HBox()
		self.radio_button1=gtk.RadioButton(None,"1")
		self.radio_button1.connect("toggled",self.radio_button_clicked,"1")
		importance_hbox.add(self.radio_button1)
		self.radio_button2 =gtk.RadioButton(self.radio_button1,"2")
		self.radio_button2.connect("toggled",self.radio_button_clicked,"2")
		importance_hbox.add(self.radio_button2)
		self.radio_button3 =gtk.RadioButton(self.radio_button1,"3")
		self.radio_button3.connect("toggled",self.radio_button_clicked,"3")
		importance_hbox.add(self.radio_button3)
		importance_table.attach(importance_hbox,0,1,1,2)

		importance_frame.add(importance_table)
		notebook.append_page(importance_frame,gtk.Label("im"))
		setting_frame.add(notebook)
		return setting_frame
	def create_alarm_list(self): #这个函数是被create_setting()调用的
		#在这里初始化self.alarm_delete_index,而不是要激活row-activated后初始化
		self.alarm_delete_index=-1
		scrolledWindow =gtk.ScrolledWindow()
		self.alarmListstore =gtk.ListStore(str)
		treeview =gtk.TreeView(self.alarmListstore)
		treeview.connect('row-activated',self.get_alarm_path)
		tvcolumn=gtk.TreeViewColumn('alarmTime')
		cell=gtk.CellRendererText()
		tvcolumn.pack_start(cell,True)
		tvcolumn.add_attribute(cell,'text',0)
		treeview.append_column(tvcolumn)
		scrolledWindow.add(treeview)
		return scrolledWindow

	def title_button_ok_clicked(self,widget):
		self.myNote.title=self.title_entry.get_text()
		self.alter.changeOneMynote(self.myNote)
		self.calendar_day_selected(widget)

	def alarm_button_new_clicked(self,widget):
		if self.alarm_button_new.get_active()==True:
			self.alarm_label.show()
			self.alarm_entry.show()
			self.tmp_hbox.show()
		elif self.alarm_button_new.get_active()==False:
			self.alarm_label.hide()
			self.alarm_entry.hide()
			self.tmp_hbox.hide()
			self.alarm_format_label.hide()
	def alarm_button_add_clicked(self,widget):
		alarmString=self.alarm_entry.get_text()
		try:
			self.alarm_format_label.hide()
			alarm=datetime.datetime.strptime(alarmString,'%Y-%m-%d %H:%M:%S')
			if self.myNote.alarm.count(alarm)!=0:
				self.alarm_format_label.set_text("has same alarm")
				self.alarm_format_label.show()
			else:
				self.myNote.alarm.append(alarm)
				self.alter.changeOneMynote(self.myNote)
				self.change_setting()
		except:
			self.alarm_format_label.set_text("match the format")
			self.alarm_format_label.show()

	def alarm_button_delete_clicked(self,widget):
		if self.alarm_delete_index !=-1:
			self.myNote.alarm.pop(self.alarm_delete_index)
			self.alter.changeOneMynote(self.myNote)
			self.change_setting()
			self.alarm_delete_index=-1
		else:
			print "no alarm selected"
	def get_alarm_path(self,treeview,path,column):
		#path是一个(i,)
		self.alarm_delete_index=path[0]

	def isOn_check_button_clicked(self,widget):
		if self.isOn_check_button.get_active()==True:
			self.myNote.isOn=1
			self.alter.changeOneMynote(self.myNote)
		elif self.isOn_check_button.get_active()==False:
			self.myNote.isOn=0
			self.alter.changeOneMynote(self.myNote)

	def radio_button_clicked(self,widget,data):
		if data =="1":
			self.myNote.importance=1
			self.alter.changeOneMynote(self.myNote)
		elif data =="2":
			self.myNote.importance=2
			self.alter.changeOneMynote(self.myNote)
		elif data =="3":
			self.myNote.importance=3
			self.alter.changeOneMynote(self.myNote)
		else:
			print "error"

	def change_setting(self):#这个函数是被oneNote_clicked调用,为了归类而放在这里
		#title
		self.title_entry.set_text(self.myNote.title)
		#alarm
		self.alarmListstore.clear()
		for i in range(len(self.myNote.alarm)):
			alarmTimeString=self.myNote.alarm[i].strftime('%Y-%m-%d %H:%M:%S')
			self.alarmListstore.append([alarmTimeString])
		#isOn
		if self.myNote.isOn == 1:
			self.isOn_check_button.set_active(True)
		elif self.myNote.isOn ==0:
			self.isOn_check_button.set_active(False)
		#radio_buttons
		if self.myNote.importance ==1:
			self.radio_button1.set_active(True)
		elif self.myNote.importance == 2:
			self.radio_button2.set_active(True)
		elif self.myNote.importance ==3:
			self.radio_button3.set_active(True)

	

if __name__ == "__main__":
	AllNotes()
	gtk.main()