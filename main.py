import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

app_id = "FOLDER_ENCRYPTER"
app_icon = ""
cat = appindicator.IndicatorCategory.APPLICATION_STATUS

if __name__ == "__main__":
    ind = appindicator.Indicator.new(app_id, app_icon, cat)
    ind.set_status(appindicator.IndicatorStatus.ACTIVE)
    