#!/usr/bin/env python

# example helloworld2.py

import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld2:
    def callback_remove(self, widget, data):
        self.box1.remove(self.button1)

    def callback_add(self, widget, data):
        self.box1.pack_start(self.button1, True, True, 0)

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Hello Buttons!")
        self.window.connect("delete_event", self.delete_event)
        self.window.set_border_width(10)
        
        self.box1 = gtk.HBox(False, 0)
        self.window.add(self.box1)
        self.button1 = gtk.Button("Button 1")
        self.button1.connect("clicked", self.callback_remove, "button 1")
        self.box1.pack_start(self.button1, True, True, 0)
        self.button1.show()
        self.button2 = gtk.Button("Button 2")
        self.button2.connect("clicked", self.callback_add, "button 2")

        self.box1.pack_start(self.button2, True, True, 0)
        self.button2.show()
        self.box1.show()
        self.window.show()

def main():
    gtk.main()

if __name__ == "__main__":
    hello = HelloWorld2()
    main()