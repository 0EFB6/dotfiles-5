# Core
from modules.core.keys import keys
assert keys
from modules.core.groups import groups
assert groups
from modules.core.layouts import layouts, floating_layout
assert layouts, floating_layout
from modules.core.screens import screens
assert screens
from modules.core.mouse import mouse
assert mouse

# Extras
from modules.extras.widgets import widget_defaults
assert widget_defaults
from modules.extras.widgets import extension_defaults
assert extension_defaults

import os
import subprocess

from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    autostart = os.path.expanduser('~/.local/bin/autostart')
    subprocess.call([autostart])

follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
# focus_on_window_activation = "smart"
# reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
