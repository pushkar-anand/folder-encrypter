import gi
import os
import foldersList
import encryptionKeyGenerator
import encrypter

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

if __name__ == "__main__":
    SECURE_KEY = encryptionKeyGenerator.key_generator(18)
    print(SECURE_KEY)

    window = gtk.Window()
    window.connect("delete_event", gtk.main_quit)
    window.set_title("Folder Encrypter")
    window.set_border_width(0)

    box1 = gtk.VBox(False, 0)
    window.add(box1)
    box1.show()

    box2 = gtk.VBox(False, 10)
    box2.set_border_width(10)
    box1.pack_start(box2, True, True, 0)
    box2.show()

    button = gtk.RadioButton(None, "radio button1")
    box2.pack_start(button, True, True, 0)
    button.show()

    window.show_all()

    gtk.main()

print()
    for folder in foldersList.folders:
        files = os.listdir(folder)
        for file in files:
            encrypter.encrypt(folder + "/" + file, )
