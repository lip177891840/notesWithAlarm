#!/usr/bin/env python

import gtk
import threading
import gobject 
from subprocess import Popen, PIPE

class SearcherProgressBar(object):
    """This is the popup with only progress-bar that pulses"""
    def __init__(self):
        self._popup = gtk.Window(gtk.WINDOW_POPUP)
        self._progress = gtk.ProgressBar()
        self._progress.set_text = gtk.Label("Searching...")
        self._popup.add(self._progress)

    def run(self, search, target):
        """Run spawns a thread so that it can return the process to the
        main app and so that we can do a little more than just execute
        a subprocess"""
        self._popup.show_all()
        self._thread = threading.Thread(target=self._search, args=(search, target))
        self._thread.start()

        #Adding a callback here makes gtk check every 0.42s if thread is done
        gobject.timeout_add(420, self._callback)

    def _search(self, cmd, target):
        """This is the thread, it makes a subprocess that it communicates with
        when it is done it calls the target with stdout and stderr as arguments"""
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        target(*p.communicate())

    def _callback(self, *args):
        """The callback checks if thread is still alive, if so, it pulses
        return true makes callback continue, while false makes it stop"""
        if self._thread.is_alive():
            self._progress.pulse()
            return True
        else:
            self._popup.destroy()
            return False

class App(object):

    def __init__(self):

        self._window = gtk.Window()
        self._window.connect("destroy", self._destroy)

        vbox = gtk.VBox()
        self._window.add(vbox)

        self.button = gtk.Button()
        self.button.set_label('Pretend to search...')
        self.button.connect('clicked', self._search)
        vbox.pack_start(self.button, False, False, 0)

        entry = gtk.Entry()
        entry.set_text("This is here to show this gui doesn't freeze...")
        entry.connect("changed", self._gui_dont_freeze)
        vbox.pack_start(entry, False, False, 0)

        self._results = gtk.Label()
        vbox.pack_start(self._results, False, False, 0)

        self._gui_never_freeze = gtk.Label("Write in entry while searching...")
        vbox.pack_start(self._gui_never_freeze, False, False, 0)

        self._window.show_all()

    def run(self):

        gtk.main()

    def _gui_dont_freeze(self, widget):

        self._gui_never_freeze.set_text(
            "You've typed: '{0}'".format(widget.get_text()))

    def _search(self, widget):
        """Makes sure you can't stack searches by making button
        insensitive, gets a new popup and runs it. Note that the run
        function returns quickly and thus this _search function too."""
        self.button.set_sensitive(False)
        self._results.set_text("")
        popup = SearcherProgressBar()
        popup.run(['sleep', '10'], self._catch_results)

    def _catch_results(self, stdout, stderr):
        """This is where we do something with the output from the subprocess
        and allow button to be pressed again."""
        self.button.set_sensitive(True)
        self._results.set_text("out: {0}\terr: {1}".format(stdout, stderr))

    def _destroy(self, *args):

        self._window.destroy()         
        gtk.main_quit()

if __name__ == "__main__":

        #This is vital for threading in gtk to work correctly
        gobject.threads_init()
        a = App()
        a.run()