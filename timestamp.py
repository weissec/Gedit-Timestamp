# Quick TimeStamp Plugin for Gedit
# W3155, 2018 
# version 0.5
#
# This file needs to be placed in ~/.local/share/gedit/plugins/
# ! GUI Settings not yet implemented !
# To change the binded KEY edit line 25 of this script.
# To change the date/time format edit line 53.

from gi.repository import GObject, Gtk, Gedit, PeasGtk, Gio
import time

class ExampleAppActivatable(GObject.Object, Gedit.AppActivatable):
    app = GObject.property(type=Gedit.App)
    __gtype_name__ = "ExampleAppActivatable"

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        self._build_time()

    def _build_time(self):
	# For combinations with CTRL or ALT (ex: Ctrl+Alt+1) type: <Primary><Alt>1
        self.app.set_accels_for_action("win.time_stamp", ("F5", None))

    def do_deactivate(self):
        self._remove_time()

    def _remove_time(self):
        # removing accelerator
        self.app.set_accels_for_action("win.time_stamp", ())

class ExampleWindowActivatable(GObject.Object, Gedit.WindowActivatable, PeasGtk.Configurable):
    window = GObject.property(type=Gedit.Window)
    __gtype_name__ = "ExampleWindowActivatable"

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        # Defining the action which was set earlier in AppActivatable.
        self._connect_item()

    def _connect_item(self):
        action = Gio.SimpleAction(name='time_stamp')
        action.connect('activate', self.action_cb)
        self.window.add_action(action)

    def action_cb(self, action, data):
        # On action add timestamp.
        doc = self.window.get_active_document()
        doc.insert_at_cursor(time.strftime("%H:%M %d/%m/%Y"))
