import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

app_id = "FOLDER_ENCR"

if __name__ == "__main__":
    ind = appindicator.Indicator.new()