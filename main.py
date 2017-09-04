import gi
import decrypter
import foldersList
import folder_chooser
import folder_remover

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

app_id = "FOLDER_ENCRYPTER"
app_icon = "emblem-nowrite"
cat = appindicator.IndicatorCategory.APPLICATION_STATUS


def decrypt(e, folder_x):
    print("Decrypting: " + folder_x)
    decrypter.decrypt_all()


def build_menu():
    menu = gtk.Menu()

    menu_list = gtk.Menu()
    for folder in foldersList.folders:
        list_item = gtk.MenuItem(folder)
        list_item.connect('activate', decrypt, folder)
        menu_list.append(list_item)

    item_decrypt = gtk.MenuItem('Decrypt')
    item_decrypt.set_submenu(menu_list)
    menu.append(item_decrypt)

    item_add = gtk.MenuItem('Add Folder or File')
    item_add.connect('activate', add_folder)
    menu.append(item_add)

    item_rm = gtk.MenuItem('Remove Folders')
    item_rm.connect('activate', remove_folder)
    menu.append(item_rm)

    menu.show_all()
    return menu


def add_folder(__):
    win = folder_chooser.FileChooserWindow()
    win.connect("delete-event", gtk.main_quit)
    win.show_all()
    gtk.main()


def remove_folder(__):
    win1 = folder_remover.FolderRemoveWindow()
    win1.connect("delete-event", gtk.main_quit)
    win1.show_all()
    gtk.main()


if __name__ == "__main__":
    ind = appindicator.Indicator.new(app_id, app_icon, cat)
    ind.set_status(appindicator.IndicatorStatus.ACTIVE)
    ind.set_menu(build_menu())
    gtk.main()
