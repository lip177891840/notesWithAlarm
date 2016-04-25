import gtk
class Alarm(gtk.Window):
	def __init__(self):
		super(Alarm,self).__init__()
		self.connect("destroy",gtk.main_quit)
		self.set_title("akarn")
		self.set_size_request(390,290)
		self.set_position(gtk.WIN_POS_CENTER)
		self.show()
		gtk.main()