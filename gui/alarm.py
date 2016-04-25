#coding:utf-8
#主窗口
import gtk, sys ,os
import threading

class Alarm:
    def __init__(self):
        self.dialog =gtk.Dialog("Alarm",None,gtk.DIALOG_MODAL,(gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
        self.dialog.set_size_request(150,120)
        screen=self.dialog.get_screen()
        self.dialog.move(screen.get_width(),0)
        #self.dialog.set_icon_from_file("2.png")
        self.create_imformation()
        self.dialog.show_all()
        self.dialog.run()
        self.dialog.destroy()
        #print "width = " + str(screen.get_width()) + ", height = " + str(screen.get_height())

    def create_imformation(self):
        label1 =gtk.Label("It's time for note1:")
        self.dialog.vbox.add(label1)
        label2 =gtk.Label("note1' imformation")
        self.dialog.vbox.add(label2)

        hbox =gtk.HBox()
        checkButton =gtk.CheckButton()
        hbox.add(gtk.Label("switch"))
        hbox.add(checkButton)
        self.dialog.vbox.add(hbox)

if __name__ == "__main__":
    Alarm()
    gtk.main()