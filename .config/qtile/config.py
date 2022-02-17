from keys import keys, mod
assert keys, mod
from groups import groups
assert groups
from layouts import layouts
assert layouts

widget_defaults = dict(
    font='CodeNewRoman Nerd Font Mono Bold',
    fontsize=18,
    padding=2,
)
extension_defaults = widget_defaults.copy()

from screens import screens
assert screens


import os
import subprocess
from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.local/bin/autostart')
    subprocess.call([home])

follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
