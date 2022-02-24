from libqtile.config import Key
from libqtile.lazy import lazy

from ..utils.settings import mod, alt, terminal


def focus_previous_group(qtile):
    group = qtile.current_screen.group
    group_index = qtile.groups.index(group)
    previous_group = group.get_previous_group(skip_empty=True)
    previous_group_index = qtile.groups.index(previous_group)
    if previous_group_index < group_index:
        qtile.current_screen.set_group(previous_group)


def focus_next_group(qtile):
    group = qtile.current_screen.group
    group_index = qtile.groups.index(group)
    next_group = group.get_next_group(skip_empty=True)
    next_group_index = qtile.groups.index(next_group)
    if next_group_index > group_index:
        qtile.current_screen.set_group(next_group)


def window_to_prev_group(qtile):
    i = qtile.groups.index(qtile.current_group)
    if qtile.current_window is not None and i != 0:
        qtile.current_window.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    i = qtile.groups.index(qtile.current_group)
    if qtile.current_window is not None and i != 6:
        qtile.current_window.togroup(qtile.groups[i + 1].name)


def toggle_minimize_all(qtile):
    group = qtile.current_screen.group
    for win in group.windows:
        win.minimized = not win.minimized
        if win.minimized is False:
            group.layout_all()

keys = [

    # Different stuff to control windows and groups
    Key([mod],         "Up",        lazy.group.prev_window()),
    Key([mod],         "Down",      lazy.group.next_window()),
    Key([mod],         "d",         lazy.function(toggle_minimize_all)),
    Key([alt],         "Tab",       lazy.screen.toggle_group()),
    Key([mod],         "Left",      lazy.function(focus_previous_group)),
    Key([mod],         "Right",     lazy.function(focus_next_group)),
    Key([mod, alt],    "Left",      lazy.function(window_to_prev_group)),
    Key([mod, alt],    "Right",     lazy.function(window_to_next_group)),

    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


    # Layout
    Key([mod], "n",               lazy.layout.normalize()),
    Key([mod], "Tab",             lazy.next_layout()),
    Key([mod,  "shift"], "Tab",   lazy.prev_layout()),
    Key([mod,  "shift"], "Up",    lazy.layout.shuffle_up()),
    Key([mod,  "shift"], "Left",  lazy.layout.shuffle_left()),
    Key([mod,  "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod,  "shift"], "Down",  lazy.layout.shuffle_down()),

    # Window
    Key([],    "KP_Enter",        lazy.window.toggle_fullscreen()),
    Key([mod], "KP_Enter",        lazy.window.toggle_floating()),
    Key([mod], "q",               lazy.window.kill()),

    # Qtile
    Key([mod],  "v",              lazy.validate_config()),
    Key([mod],  "r",              lazy.reload_config()),
    Key([mod, "shift"], "r",      lazy.restart()),
    Key([mod, "shift"], "q",      lazy.shutdown()),
    Key([mod, "shift"], "b",      lazy.hide_show_bar()),

    # Apps
    Key([mod], "Return",
        lazy.spawn(terminal)),
    Key([mod], "f",
        lazy.spawn("nemo")),
    Key([mod], "w",
        lazy.spawn("rofi -mode window -show window")),
    Key([mod], "space",
        lazy.spawn("rofi -show drun -terminal alacritty -show-icons")),
    Key([mod], "x",
        lazy.spawn("nwgbar")),
    Key([mod], "b",
        lazy.spawn("google-chrome-beta")),
    Key([mod], "t",
        lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], "y",
        lazy.spawn("google-chrome-beta --app=https://www.youtube.com")),
    Key([mod], "s",
        lazy.spawn("gnome-control-center")),
    Key([mod], "k",
        lazy.spawn("/home/ervin/.local/bin/qtile_key_pdf")),
    Key([mod], "l",
        lazy.spawn("betterlockscreen -l dimblur")),
    Key([mod], "m",
        lazy.spawn("/home/ervin/.local/bin/start-spotify")),

    # DE keys
    Key([], "Print",
        lazy.spawn("flameshot screen -p /home/ervin/Pictures")),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("/home/ervin/.local/bin/vol_ctl +5%")),
    Key([], "XF86AudioMute",
        lazy.spawn("/home/ervin/.local/bin/vol_mute")),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("/home/ervin/.local/bin/vol_ctl -5%")),
    Key([], "XF86AudioPrev",
        lazy.spawn("/home/ervin/.local/bin/media_ctl previous")),
    Key([], "XF86AudioPlay",
        lazy.spawn("/home/ervin/.local/bin/media_ctl play-pause")),
    Key([], "XF86AudioNext",
        lazy.spawn("/home/ervin/.local/bin/media_ctl next")),
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("/home/ervin/.local/bin/brightness_ctl up")),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("/home/ervin/.local/bin/brightness_ctl down")),
    Key([alt], "space",
        lazy.widget["keyboardlayout"].next_keyboard()),
]
