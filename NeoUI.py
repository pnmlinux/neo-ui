import gi, time, datetime, psutil, sys, threading
gi.require_version('Gtk','3.0')
from get_data import *
from gi.repository import Gtk

#Window

class Main:
    def __init__(self):
        global t1, stop

        #Set Glade File

        gladefile = "mainwindow.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladefile)

        #Get Objects

        mainwindow = self.builder.get_object("main-window")
        logo = self.builder.get_object("os-logo")
        kerneltext = self.builder.get_object("kernel-text")
        cputext = self.builder.get_object("cpu-text")
        gputext = self.builder.get_object("gpu-text")
        detext = self.builder.get_object("de-text")
        memtext = self.builder.get_object("mem-text")
        uptimetext = self.builder.get_object("uptime-text")
        #Uptime Function
        def close(self, widget):
            sys.exit()
        def uptime():

            total_seconds = time.time() - psutil.boot_time()
            total_seconds = int(total_seconds)
            while True:
                timer = datetime.timedelta(seconds = total_seconds)
                time.sleep(1)
                total_seconds+=1
                timer = str(timer)
                uptimetext.set_text("Uptime: "+timer)
        
        mainwindow.connect("delete-event", close)
        mainwindow.show_all()
        logo.new_from_file(oslogo())
        kerneltext.set_text("Kernel : "+kernel())
        cputext.set_text("CPU : "+cpu())
        gputext.set_text("GPU : "+gpu())
        detext.set_text("Desktop : "+desktopenv())
        memtext.set_text("RAM : "+mem())
        t1 = threading.Thread(target=uptime)
        t1.start()
        Gtk.main()

if __name__ == "__main__":
    Main()