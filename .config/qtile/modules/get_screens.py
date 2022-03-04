import subprocess

from libqtile import bar
from libqtile.config import Screen

from .widgets import primary_widgets, secondary_widgets
from .settings import colors


def statusbar(widgets):
    return bar.Bar(
        widgets,
        25,
        margin=3,
        background=colors[0])


widgets1 = primary_widgets()
widgets2 = secondary_widgets()

screens = [
    Screen(top=statusbar(widgets1)),
    Screen(top=statusbar(widgets2)),
]

command = subprocess.run(
    "xrandr --output HDMI1 --right-of eDP1 --auto", shell=True)

if command.returncode != 0:
    connected_monitors = 1
else:
    connected_monitors = 2

if connected_monitors == 2:
    screens.append(Screen(top=statusbar(widgets2)))
