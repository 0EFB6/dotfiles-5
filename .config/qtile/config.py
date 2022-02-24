import os
import subprocess
from libqtile import bar, layout, qtile, hook, widget
from libqtile.config import (
    Click,
    Drag,
    Group,
    Key,
    Match,
    Screen,
    DropDown,
    ScratchPad
)
from libqtile.lazy import lazy

# from modules.widgets import (
#     widgets_top_screen1,
#     widgets_top_screen2,
#     colors_nord
# )

mod = "mod4"
alt = "mod1"
terminal = "alacritty"


@hook.subscribe.startup_once
def autostart():
    autostart = os.path.expanduser('~/.local/bin/autostart')
    subprocess.call([autostart])


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


def no_text(text):
    return ''


def reload():
    # qtile.cmd_reload_config()
    qtile.cmd_restart()
    qtile.cmd_spawn('/home/ervin/.local/bin/change_wallpaper')


keys = [

    # Different stuff to control windows and groups
    Key([mod], "Up", lazy.group.prev_window()),
    Key([mod], "Down", lazy.group.next_window()),
    Key([mod], "d", lazy.function(toggle_minimize_all)),
    Key([alt], "Tab", lazy.screen.toggle_group()),
    Key([mod], "Left", lazy.function(focus_previous_group)),
    Key([mod], "Right", lazy.function(focus_next_group)),
    Key([mod, alt], "Left", lazy.function(window_to_prev_group)),
    Key([mod, alt], "Right", lazy.function(window_to_next_group)),

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
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),

    # Window
    Key([], "KP_Enter", lazy.window.toggle_fullscreen()),
    Key([mod], "KP_Enter", lazy.window.toggle_floating()),
    Key([mod], "q", lazy.window.kill()),

    # Qtile
    Key([mod], "v", lazy.validate_config()),
    Key([mod], "r", lazy.reload_config()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([mod, "shift"], "b", lazy.hide_show_bar()),

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

groups = []

group_names = 'coding www social settings etc media'.split()
group_labels = ["", "", "", "", "", ""]
group_layouts = ["bsp", "max", "zoomy", "bsp", "bsp", "monadthreecol"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i],
            label=group_labels[i]
        ))

groups.append(
    ScratchPad(
        "scratchpad",
        [DropDown("term", terminal, opacity=0.8)]))


@hook.subscribe.client_new
def assign_app_group(client):
    from modules.matches import d
    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)


for i, name in enumerate(group_names, 1):
    keys.extend([
        Key([mod], str(i), lazy.group[name].toscreen()),
        Key([mod, 'shift'], str(i), lazy.window.togroup(name))])

layouts = [
    layout.Bsp(
        margin=5,
        fontsize=20,
        border_width=1,
        border_focus="#bcadf9"
    ),
    layout.Zoomy(  # !!CHECK DOCS FOR THIS ONE!!
        margin=5,
        columnwidth=150,
        fontsize=20,
        border_width=1
    ),
    layout.Max(
        margin=5,
        fontsize=20,
    ),
    layout.MonadTall(
        margin=5,
        fontsize=20,
        border_width=1,
        border_focus="#bcadf9"
    ),
    layout.MonadWide(
        margin=5,
        border_width=1,
        border_focus="#bcadf9",
        max_ratio=0.9
    ),
    layout.MonadThreeCol(
        margin=5,
        border_width=0,
        ratio=0.33,
        max_ratio=0.95
    ),
    # layout.Slice(
    #     width=455,
    #     match=Match(wm_class=["firefox"])
    #     ),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ],
    border_width=0)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

widget_defaults = dict(
    font="CodeNewRoman Nerd Font Mono Bold",
    fontsize=15,
    padding=3,
)

extension_defaults = widget_defaults.copy()

colors_nord = ["#2e3440",   # 0
               "#3b4252",   # 1
               "#434c5e",   # 2
               "#4c566a",   # 3
               "#d8dee9",   # 4
               "#e5e9f0",   # 5
               "#eceff4",   # 6
               "#8fbcbb",   # 7
               "#88c0d0",   # 8
               "#81a1c1",   # 9
               "#5e81ac",   # 10
               "#bf616a",   # 11
               "#d08770",   # 12
               "#ebcb8b",   # 13
               "#a3be8c",   # 14
               "#b48ead",   # 15
               ]

common_widgets = [
    widget.Image(
        filename="/usr/share/pixmaps/archlinux-logo.svg",
        margin=5,
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
            "rofi -show drun -terminal alacritty -show-icons")}
    ),
    widget.Image(
        filename="/usr/share/icons/Papirus/64x64/apps/python.svg",
        margin=5,
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
            "subl /home/ervin/.config/qtile/config.py")}
    ),
    widget.TextBox(
        text='/',
        foreground=colors_nord[3],
        background=colors_nord[0],
        padding=0,
        fontsize=35
    ),
    widget.GroupBox(
        font='Font Awesome 6 Free Solid',
        fontsize=12,
        highlight_method='block',
        block_highlight_text_color=colors_nord[4],
        inactive=colors_nord[3],
        active=colors_nord[4],
        padding_y=7,
        rounded="true"
    ),
    widget.TextBox(
        text='/',
        foreground=colors_nord[3],
        background=colors_nord[0],
        padding=0,
        fontsize=35
    ),
    # widget.CurrentLayoutIcon(
    #     scale=0.6
    #     ),
    widget.CurrentLayout(),
    widget.TextBox(
        text='/',
        foreground=colors_nord[3],
        background=colors_nord[0],
        padding=0,
        fontsize=35
    ),
    widget.TaskList(
        parse_text=no_text,
        highlight_method='block',
        icon_size=19,
        border=colors_nord[3],
        margin=5,
        rounded=False,
        padding_x=3
    ),
    widget.WidgetBox(
        widgets=[
            widget.Clock(
                format='%A, %B %d - ',
                padding=0,
                foreground=colors_nord[6],
                fontsize=18
            ),
        ],
        foreground=colors_nord[6],
        text_closed="\uf017 ",
        text_open="\uf017 ",
        font='Font Awesome 6 Free Solid',
        fontsize=11
    ),
    widget.Clock(
        format='%H:%M',
        padding=0,
        foreground=colors_nord[6],
    ),
    widget.Spacer(
        length=bar.STRETCH
    )
]

widgets_top_screen1 = [
    widget.TextBox(
        font='Font Awesome 6 Free Solid',
        text="",
        foreground=colors_nord[15]
    ),
    widget.Volume(
        foreground=colors_nord[15],
        mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")}
    ),
    widget.TextBox(
        text='/',
        foreground=colors_nord[3],
        background=colors_nord[0],
        padding=0,
        fontsize=35
    ),
    widget.TextBox(
        font='Font Awesome 6 Free Solid',
        text="",
        fontsize=15,
        foreground=colors_nord[14],
        background=colors_nord[0],
    ),
    widget.KeyboardLayout(
        configured_keyboards=["us", "ro std"],
        display_map={'us': 'us', 'ro std': 'ro'},
        foreground=colors_nord[14],
        background=colors_nord[0],
    ),
    widget.TextBox(
        text='/',
        foreground=colors_nord[3],
        background=colors_nord[0],
        padding=0,
        fontsize=35
    ),
    widget.TextBox(
        font='Font Awesome 6 Free Solid',
        text="",
        fontsize=15,
        foreground=colors_nord[5],
        background=colors_nord[0],
    ),
    widget.GenPollText(
        update_interval=3600,
        foreground=colors_nord[5],
        func=lambda: subprocess.check_output(
            "/home/ervin/.local/bin/chkup"
        ).decode("utf-8"),
        mouse_callbacks={'Button1':
                         lambda: qtile.cmd_spawn("alacritty -e yay")}
    ),
    widget.TextBox(
        text='/',
        foreground=colors_nord[3],
        background=colors_nord[0],
        padding=0,
        fontsize=35
    ),
    widget.TextBox(
        font='Font Awesome 6 Free Solid',
        text="",
        padding=2,
        foreground=colors_nord[13]
    ),
    widget.Spacer(
        length=3),
    widget.Backlight(
        padding=0,
        backlight_name="intel_backlight",
        foreground=colors_nord[13]
    ),
    widget.TextBox(
        text='/',
        foreground=colors_nord[3],
        background=colors_nord[0],
        padding=0,
        fontsize=35
    ),
    widget.Systray(
        icon_size=16,
        padding=3
    ),
    widget.TextBox(
        text='/',
        foreground=colors_nord[3],
        background=colors_nord[0],
        padding=0,
        fontsize=35
    ),
    widget.Battery(
        format="{percent:2.0%}",
        update_interval=5,
        foreground=colors_nord[14]
    ),
    widget.GenPollText(
        update_interval=1,
        foreground=colors_nord[14],
        font="Font Awesome 6 Free Solid",
        func=lambda:
        subprocess.check_output(
            "/home/ervin/.local/bin/bat_icon"
        ).decode('utf-8')
    ),
    widget.GenPollText(
        update_interval=1,
        foreground=colors_nord[14],
        font="Font Awesome 6 Free Solid",
        fontsize=11,
        func=lambda:
        subprocess.check_output(
            "/home/ervin/.local/bin/bat_charging_icon"
        ).decode('utf-8')
    ),
    widget.TextBox(
        text='/',
        foreground=colors_nord[3],
        background=colors_nord[0],
        padding=0,
        fontsize=35
    ),
    widget.TextBox(
        text='',
        font="Font Awesome 6 Free Solid",
        mouse_callbacks={'Button1': lambda: reload()},
        foreground=colors_nord[10],
        padding=0),
    widget.Spacer(
        length=5),
    widget.GenPollText(
        update_interval=3600,
        foreground=colors_nord[13],
        func=lambda: subprocess.check_output(
            "/home/ervin/.local/bin/uptime.sh").decode("utf-8")
    ),
    widget.Spacer(
        length=5),
    widget.TextBox(
        text="",
        font="Font Awesome 6 Free Solid",
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('nwgbar')},
        foreground=colors_nord[11]
    ),
    widget.Spacer(
        length=5),
]

widgets_top_screen1[0:0] = common_widgets

widgets_top_screen2 = [
    widget.TextBox(
        font='Font Awesome 6 Free Solid',
        text="",
        fontsize=15,
        foreground=colors_nord[5],
        background=colors_nord[0],
    ),
    widget.GenPollText(
        update_interval=3600,
        foreground=colors_nord[5],
        func=lambda: subprocess.check_output(
            "/home/ervin/.local/bin/chkup"
        ).decode("utf-8"),
        mouse_callbacks={'Button1':
                         lambda: qtile.cmd_spawn("alacritty -e yay")}
    ),
    widget.TextBox(
        text='/',
        foreground=colors_nord[3],
        background=colors_nord[0],
        padding=0,
        fontsize=35
    ),
    widget.TextBox(
        font='Font Awesome 6 Free Solid',
        text="",
        padding=2,
        foreground=colors_nord[13]
    ),
    widget.Spacer(
        length=3),
    widget.Backlight(
        padding=0,
        backlight_name="intel_backlight",
        foreground=colors_nord[13]
    ),
    widget.TextBox(
        text='/',
        foreground=colors_nord[3],
        background=colors_nord[0],
        padding=0,
        fontsize=35
    ),
]

widgets_top_screen2[0:0] = common_widgets


screens = [
    Screen(
        top=bar.Bar(
            widgets_top_screen1,
            25,
            margin=3,
            background=colors_nord[0]
        ),
    ),
    Screen(
        top=bar.Bar(
            widgets_top_screen2,
            25,
            margin=3,
            background=colors_nord[0]
        ),
    ),
]

follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
