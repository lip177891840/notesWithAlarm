#coding=utf-8
import gtk,os,sys

class Help(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self)
		self.set_title("Help")
		self.set_size_request(300,200)
		self.add(gtk.Label("This window has not been designed\n"
			"for some reasons"))
		self.show_all()
		#self.connect("delete_event",self.exit)
if __name__ =="__main__":
	Help()
	gtk.main()