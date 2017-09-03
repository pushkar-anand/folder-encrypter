import gi
import json
import foldersList
import decrypter

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk


class FolderRemoveWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self, title="Select folder to remove")

        box = gtk.Box(spacing=6)
        self.add(box)

        for folder in foldersList.folders:
            button = gtk.Button(folder)
            button.connect("clicked", self.removefolder, folder)
            box.add(button)

    def removefolder(self, x, folder_to_delete):
        print(folder_to_delete)
        x = 0
        with open('folder.json', 'r+') as data_file:
            data = json.load(data_file)
            folderList = data["folders"]
            for folder in folderList:
                if folder == folder_to_delete:
                    x = 1
                    break
            if (x == 1):
                folderList.remove(folder_to_delete)
                print(folderList)
                data_file.seek(0)
                new_json = "{\"folders\":" + json.dumps(folderList) + "}"
                print(new_json)
                data_file.write(new_json)
                data_file.truncate()
            decrypter.decrypt(folder_to_delete)
        gtk.Window.destroy(self)

