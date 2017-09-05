import gi
import first_run
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


class UserKeyInput(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Enter Your key")
        self.set_size_request(200, 100)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        vbox.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)
        button = Gtk.Button.new_with_mnemonic("_Continue")
        button.connect("clicked", self._continue)
        hbox.pack_start(button, True, True, 0)

    def _continue(self, button):
        self.passphrase = self.entry.get_text()
        print(self.passphrase)
        first_run.start_encryption(key)



# win = UserKeyInput()
# win.connect("delete-event", Gtk.main_quit)
# win.show_all()
# Gtk.main()
