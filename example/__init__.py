from gi.repository import GLib, GObject, Gio, Gtk, Gedit


class ExampleWinActivatable(GObject.Object, Gedit.WindowActivatable):

    window = GObject.property(type=Gedit.Window)
    
    def do_activate(self):
        print('Hello world!')
        dialog = Gtk.MessageDialog(self.window,
                                   Gtk.DialogFlags.MODAL,
                                   Gtk.MessageType.INFO,
                                   Gtk.ButtonsType.OK,
                                   "Hello World")
        
        dialog.connect('response', self._dialog_responded, None)
        dialog.show()
    
    def _dialog_responded(self, dialog, response_id, user_data):
        dialog.hide()
    
    def do_deactivate(self):
        pass
    
    def do_update_state(self):
        pass
