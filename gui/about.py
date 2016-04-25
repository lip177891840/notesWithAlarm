#coding:utf-8

import gtk

class About(gtk.AboutDialog):
	def __init__(self):
		super(About,self).__init__()
		logo="images/2.png"
		self.set_logo(gtk.gdk.pixbuf_new_from_file(logo))
		self.set_icon_from_file(logo)
		self.set_name("NotesWithAlarm")
		self.set_version("0.1")
		self.set_comments("A Notebook with alarm")
		self.set_copyright("Copyright © 2015 lip")
		self.set_website("https://github.com/lip177891840/notesWithAlarm")
		self.set_website_label("Homepage")

		self.set_authors(["lip<177891840@qq.com>"])
		self.set_translator_credits("lip<177891840@qq.com>")

		self.set_license("Copyright(c) 2015,lip\n\n"\
			"NotesWithAlarm is free software,you can redistribute id or modify\n"\
			"it under the terms of the GNU General Public License as published by\n"\
			"the Free Software Foundation; either version 0.1 of the License, or\n"\
			"(at your option) any later version.\n\n"\
			"NotesWithAlarm is distributed in the hope that it will be useful,\n"
			"if you have any new idea about NotesWithAlarm,you can improve it.\n"
			"you have any question about it,you can write to <177891840@qq.com>\n"
			"and i'm pleasure to slove your questions"
			)
		

		self.show_all()
		self.run()
		self.destroy()


if __name__ == "__main__":
	About()
