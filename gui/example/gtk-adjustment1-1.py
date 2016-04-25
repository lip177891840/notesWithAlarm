# ensure that PyGTK 2.0 is loaded - not an older version
import pygtk
pygtk.require('2.0')
# import the GTK module
import gtk

class MyGUI:

  def __init__( self, title):
    self.window = gtk.Window()
    self.title = title
    self.window.set_title( title)
    self.window.set_size_request( 200, 100)
    self.window.connect( "destroy", self.destroy)
    self.create_interior()
    self.window.show_all()

  def create_interior( self):
    self.mainbox = gtk.VBox()
    self.window.add( self.mainbox)
    # label for value display
    self.label = gtk.Label()
    self.label.show()
    # adjustment
    adj = gtk.Adjustment( value=10, lower=0, upper=30, step_incr=1, page_incr=10, page_size=0) #@+
    adj.connect( "value_changed", self.adjustment_changed) #@+
    adj.emit( "value_changed") # force update of label #@+
    # scrollbar - we provide our own Adjustment, otherwise scrollbar creates a new one for us
    sb = gtk.HScrollbar( adjustment=adj) #@+
    sb.show()
    # pack the widgets
    self.mainbox.pack_start( self.label)
    self.mainbox.pack_start( sb, expand=False)
    # show the box
    self.mainbox.show()

  def adjustment_changed( self, adj):
    self.label.set_label( "%.2f" % adj.value)

  def main( self):
    gtk.main()

  def destroy( self, w):
    gtk.main_quit()

if __name__ == "__main__":
  m = MyGUI( "Adjustment example")
  m.main()
