import subprocess

from libqtile import bar
from libqtile.config import Screen
from libqtile.log_utils import logger

from .widgets import (
    colors_nord,
    primary_widgets,
    secondary_widgets,
)


def statusbar(widgets):
    return bar.Bar(
        widgets,
        25,
        margin=3,
        background=colors_nord[0])


widgets1 = primary_widgets()
widgets2 = secondary_widgets()

screens = [
    Screen(top=statusbar(widgets1)),
    Screen(top=statusbar(widgets2)),
]

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(top=statusbar(secondary_widgets)))
