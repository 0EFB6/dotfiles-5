import subprocess
from libqtile import bar
from libqtile.config import Screen
from libqtile.command import lazy

from widgets import (
    widgets_top_screen1,
    widgets_top_screen2,
    colors_nord
    )

screens = [
    Screen(
        top=bar.Bar(
            widgets_top_screen1,
            25,
            margin=3,
            background=colors_nord[0]
        ),
    ),
]

displays = subprocess.check_output('xrandr').decode('utf-8')
display_status = displays.find('disconnected')

if display_status == -1:
    lazy.spawn(
        "xrandr --output eDP-1 --auto --output HDMI-1 --auto --right-of eDP-1")
    screens.append(
        Screen(
            top=bar.Bar(
                widgets_top_screen2,
                25,
                margin=3,
                background=colors_nord[0]
                ),
            ),
        )
