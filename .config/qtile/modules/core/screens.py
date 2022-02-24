from libqtile import bar
from libqtile.config import Screen

from ..extras.widgets import widgets_top_screen1, widgets_top_screen2
from ..utils.settings import colors

screens = [
    Screen(
        top=bar.Bar(
            widgets_top_screen1,
            25,
            margin=3,
            background=colors[0]
        ),
    ),
    Screen(
        top=bar.Bar(
            widgets_top_screen2,
            25,
            margin=3,
            background=colors[0]
        ),
    ),
]
