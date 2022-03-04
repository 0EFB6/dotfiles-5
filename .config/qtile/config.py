from os import path
import subprocess


try:
    import aiomanhole
except ImportError:
    aiomanhole = None

from libqtile import hook
from modules.keys import keys
from modules.groups import groups
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse
from modules.settings import widget_defaults, extension_defaults
from modules.get_screens import screens
assert keys
assert groups
assert layouts
assert floating_layout
assert mouse
assert widget_defaults
assert extension_defaults
assert screens


if aiomanhole:
    @hook.subscribe.startup_complete
    def set_manhole():
        aiomanhole.start_manhole(
        port=7113,
        namespace={"qtile": qtile})  # noqa


@hook.subscribe.startup_once
def autostart():
    autostart = path.expanduser('~/.local/bin/autostart')
    subprocess.call([autostart])


follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
