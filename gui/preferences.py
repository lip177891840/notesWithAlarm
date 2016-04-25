#coding:utf-8
import gtk
import pygtk

class Preferences(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self)
		self.set_size_request(500,300)
		self.set_title("Preferences")
		#self.connect("delete_event",gtk.main_quit)

		table =gtk.Table(10,5,True)
		notebook = gtk.Notebook()
		frame1=gtk.Frame("frame1")
		frame1.add(gtk.Label("This window has not been designed\nfor some reasons"))
		notebook.append_page(frame1,gtk.Label("page1"))
		notebook.append_page(gtk.Frame("frame2"),gtk.Label("page2"))
		table.attach(notebook,0,5,0,9)

		okButton =gtk.Button("Ok")
		okButton.set_size_request(20,20)
		#okButton.connect("clicked",self.okButton_clicked)
		table.attach(okButton,3,4,9,10)

		cancleButton =gtk.Button("Cancle")
		#cancleButton.connect("clicked",self,cancleButton_clicked)
		table.attach(cancleButton,4,5,9,10)
		self.add(table)
		self.show_all()


if __name__ =="__main__":
	Preferences()
	gtk.main()