#coding:utf-8
# 这是一个便签,但是带有提醒功能,也是我一直在寻找的这种功能的软件,
# 但是没有找到一个特别合适的,早就有自己开发一个这样功能的便签本的想法了,现在终于要动手了.

import gtk
import appindicator
import pygame
import os, sys

from gui.newNote import NewNote
from gui.allNotes import AllNotes
from gui.about import About
from gui.preferences import Preferences
from gui.help import Help
from myTimer import MyTimer

baseDir=os.getcwd()

version ="0.1"

if __name__ == "__main__":

	try:
		indicator= appindicator.Indicator("notesWithAlarm",os.path.abspath("images/2.png"),appindicator.CATEGORY_APPLICATION_STATUS)
		indicator.set_status(appindicator.STATUS_ACTIVE)
	
		#菜单项new, "添加新的笔记" 
		menu =gtk.Menu()
		#-----------New  AllNotes----------------------
		new =gtk.MenuItem("New")
		menu.append(new)
		new.connect("activate",lambda w: NewNote())
		new.show()

		allNotes =gtk.MenuItem("All Notes")
		menu.append(allNotes)
		allNotes.connect("activate",lambda w: AllNotes())
		allNotes.show()

		sep1 =gtk.SeparatorMenuItem()
		menu.append(sep1)
		sep1.show()

		sep2 =gtk.SeparatorMenuItem()
		menu.append(sep2)
		sep2.show()
		#--------------preferences help about----------------

		preferences =gtk.MenuItem("Preferences")
		menu.append(preferences)
		preferences.connect("activate",lambda w: Preferences())
		preferences.show()

		help =gtk.MenuItem("Help")
		menu.append(help)
		help.connect("activate",lambda w: Help())
		help.show()

		about =gtk.MenuItem("About")
		menu.append(about)
		about.connect("activate",lambda w: About())
		about.show()

		sep =gtk.SeparatorMenuItem()
		menu.append(sep)
		sep.show()

		#-------quit--------------
		quit =gtk.ImageMenuItem(gtk.STOCK_QUIT)
		quit.connect("activate", gtk.main_quit)
		menu.append(quit)
		quit.show()

		#==========  myTimer  ===========
		#lambda w: MyTimer()
	
		indicator.set_menu(menu)
		gtk.main()

	except (KeyboardInterrupt, SystemExit):
		print "Bye"
