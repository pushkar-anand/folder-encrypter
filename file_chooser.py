import gi
import encrypter
import json

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk


class FileChooserWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self, title="Folder Selection")

        box = gtk.Box(spacing=6)
        self.add(box)

        button1 = gtk.Button("Choose Folder")
        button1.connect("clicked", self.on_folder_clicked)
        box.add(button1)


    def on_folder_clicked(self, widget):
        x=1
        dialog = gtk.FileChooserDialog("Please choose a folder", self,
                                       gtk.FileChooserAction.SELECT_FOLDER,
                                       (gtk.STOCK_CANCEL, gtk.ResponseType.CANCEL,
                                        "Select", gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == gtk.ResponseType.OK:
            selected_folder = dialog.get_filename()
            with open('folder.json', 'r+') as data_file:
                data = json.load(data_file)
                folderList = data["folders"]
                for folder in folderList:
                    if folder == selected_folder:
                        x = 0
                        break
                if(x==1):
                    new_folder_list = folderList + [selected_folder]
                    print(new_folder_list)
                    data_file.seek(0)
                    new_json = "{\"folders\":" +json.dumps(new_folder_list)+ "}"
                    print(new_json)
                    data_file.write(new_json)
                    data_file.truncate()
                    encrypter.encrypt(selected_folder)

        elif response == gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        dialog.destroy()
        gtk.Window.destroy(self)

