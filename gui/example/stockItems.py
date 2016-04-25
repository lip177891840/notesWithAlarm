#!/usr/bin/env python

# example helloworld2.py

import pygtk
import gtk

class stockItems(gtk.Window):

    def __init__(self):
        super(stockItems,self).__init__()
        self.set_title("Hello Buttons!")
        self.set_size_request(1000,100)


        list =gtk.stock_list_ids()
        print list[89]
        print list[38]

        toolbar =gtk.Toolbar()
        box1 = gtk.HBox(False, 0)
        print len(list) #105
        for i in range(len(list)):
        	toolbutton =gtk.ToolButton(list[i])
        	toolbutton.set_tooltip_text(str(i))
        	toolbar.insert(toolbutton,i)
        box1.add(toolbar)
        self.add(box1)
        self.show_all()

def main():
    gtk.main()

if __name__ == "__main__":
    hello = stockItems()
    main()