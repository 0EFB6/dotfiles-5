import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess


def window_icon():
    icon_name = subprocess.check_output("/home/ervin/.scripts/window_icon").decode('utf-8')
    if icon_name:
        theme = Gtk.IconTheme.get_default()
        found_icons = set()
        for res in range(0, 512, 2):
            icon = theme.lookup_icon(icon_name, res, 0)
            if icon:
                found_icons.add(icon.get_filename())
        found_icons = sorted(found_icons, key=str.lower)
        if found_icons:
            return found_icons[0]
        else:
            return [icon_name, "was not found"]
