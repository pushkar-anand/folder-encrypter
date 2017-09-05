import os
import foldersList
import encryptionKeyGenerator
import encrypter
import gi
import userKeyInput

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Folder Encryption")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Generate Key")
        button.connect("clicked", self.generate_key)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Use your own Key")
        button.connect("clicked", self.user_key)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Close")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def generate_key(self, button):
        gen_key = encryptionKeyGenerator.key_generator(20)
        self.launch_encryption_window(gen_key)
        print("\"Generate button\" button was clicked")

    def user_key(self, button):
        self.launch_get_user_key()
        print("\"Open\" button was clicked")

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

    def launch_encryption_window(self, key):
        print("enc window")
        start_encryption(key)

    def launch_get_user_key(self):
        Gtk.Window.destroy(self)
        winu = userKeyInput.UserKeyInput()
        winu.connect("delete-event", Gtk.main_quit)
        winu.show_all()

        print("in launc")


if __name__ == '__main__':
    win = ButtonWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


def start_encryption(key):
    for folder in foldersList.folders:
        files = os.listdir(folder)
        for file in files:
            encrypter.first_encrypt(folder + "/" + file, key)
