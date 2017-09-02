import gi
import first_run
import decrypter
import foldersList

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

app_id = "FOLDER_ENCRYPTER"
app_icon = "emblem-nowrite"
cat = appindicator.IndicatorCategory.APPLICATION_STATUS


def decrypt():
    decrypter.decrypt_all()


def build_menu():
    menu = gtk.Menu()

    menu_list = gtk.Menu()
    for folder in foldersList.folders:
        list_item = gtk.MenuItem(folder)
        menu_list.append(list_item)

    item_decrypt = gtk.MenuItem('Decrypt')
    item_decrypt.set_submenu(menu_list)
    menu.append(item_decrypt)
    item_stop = gtk.MenuItem('Add Folders')
    # item_stop.connect('activate', stop)
    menu.append(item_stop)

    item_quit = gtk.MenuItem('Remove Folders')
    # item_quit.connect('activate', quit)
    menu.append(item_quit)

    menu.show_all()
    return menu


if __name__ == "__main__":
    ind = appindicator.Indicator.new(app_id, app_icon, cat)
    ind.set_status(appindicator.IndicatorStatus.ACTIVE)
    ind.set_menu(build_menu())
    gtk.main()
