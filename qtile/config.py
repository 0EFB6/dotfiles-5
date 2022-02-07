import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import (
    Click,
    Drag,
    DropDown,
    Group,
    Key,
    Match,
    ScratchPad,
    Screen,
)
from libqtile.command import lazy


mod = "mod4"
terminal = "alacritty"


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
    Key([mod],         "Left",      lazy.function(focus_previous_group)),
    Key([mod],         "Right",     lazy.function(focus_next_group)),
    Key([mod],         "d",         lazy.function(toggle_minimize_all)),
    Key([mod, "mod1"], "Left",      lazy.function(window_to_prev_group)),
    Key([mod, "mod1"], "Right",     lazy.function(window_to_next_group)),

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
    Key([mod,  "shift"], "r",     lazy.restart()),
    Key([mod,  "shift"], "q",     lazy.shutdown()),
    Key([mod],  "r",              lazy.reload_config()),
    Key([mod],  "v",              lazy.validate_config()),

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
        lazy.spawn("google-chrome-stable")),
    Key([mod], "t",
        lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], "y",
        lazy.spawn("google-chrome-stable --app=https://www.youtube.com")),
    Key([mod], "s",
        lazy.spawn("gnome-control-center")),
    Key([mod], "k",
        lazy.spawn("/home/ervin/.local/bin/qtile_key_pdf")),

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
        lazy.spawn("playerctl -a previous")),
    Key([], "XF86AudioPlay",
        lazy.spawn("playerctl -a play-pause")),
    Key([], "XF86AudioNext",
        lazy.spawn("playerctl -a next")),
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("/home/ervin/.local/bin/brightness_ctl up")),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("/home/ervin/.local/bin/brightness_ctl down")),
    Key(["mod1"], "space",
        lazy.widget["keyboardlayout"].next_keyboard()),
]

groups = []

group_names = 'coding media www social settings etc'.split()
group_labels = ["", "", "", "", "", ""]
group_layouts = ["bsp", "monadtall", "max", "zoomy", "bsp", "bsp"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i]
        ))

groups.append(
    ScratchPad(
        "scratchpad",
        [DropDown("term", terminal, opacity=0.8)]))


@hook.subscribe.client_new
def assign_app_group(client):
    d = {}
    d[group_names[0]] = [
        "terminator",
        "atom",
        "geany",
        "brackets",
        "code-oss",
        "code",
        "thunar",
        "nemo",
        "caja",
        "nautilus",
        "org.gnome.nautilus",
        "pcmanfm",
        "pcmanfm-qt",
        "Atom",
        "Alacritty",
        "Sublime_text",
        "sublime_text",
        "Geany",
        "Brackets",
        "Code-oss",
        "Code",
        "Thunar",
        "Nemo",
        "Caja",
        "Nautilus",
        "org.gnome.Nautilus",
        "Pcmanfm",
        "Pcmanfm-qt",
        "evince",
        ]
    d[group_names[1]] = [
        "www.youtube.com",
        "Spotify",
        "Pragha",
        "Clementine",
        "Deadbeef",
        "Audacious",
        "spotify",
        "pragha",
        "clementine",
        "deadbeef",
        "audacious",
        "anbox",
        "TelegramDesktop",
        "Discord",
        "telegramDesktop",
        "discord",
        "Vlc",
        "vlc",
        "Mpv",
        "mpv",
        "obs",
        ]
    d[group_names[2]] = [
        "Firefox",
        "firefox",
        "Navigator",
        "Chromium",
        "chromium",
        "google-chrome",
        "Google-chrome",
        "docs.google.com__spreadsheets_d_1n-rQuzX04B-40f-xlXRoTUjcCqWrpj2qKNtjCUHER7c_edit"
        "qbittorrent",
        ]
    d[group_names[3]] = [
        "ferdi",
        ]
    d[group_names[4]] = [
        "gnome-control-center",
        "blueman-manager",
        "nitrogen",
        "pling-store",
        "Xfce4-power-manager-settings",
        "pavucontrol"
        ]

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
        border_focus="#bcadf9"
        ),
]

widget_defaults = dict(
    font='CodeNewRoman Nerd Font Mono Bold',
    fontsize=17,
    padding=2,
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


def no_text(text):
    return ''


def reload():
    qtile.cmd_reload_config()
    qtile.cmd_spawn('/home/ervin/.local/bin/change_wallpaper.sh')


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename="/usr/share/pixmaps/archlinux-logo.svg",
                    margin=5,
                    mouse_callbacks=
                    {'Button1': lambda: qtile.cmd_spawn("rofi -show drun -terminal alacritty -show-icons")}
                    ),
                widget.Image(
                    filename="/usr/share/icons/Papirus/64x64/apps/python.svg",
                    margin=5,
                    mouse_callbacks=
                    {'Button1': lambda: qtile.cmd_spawn("subl /home/ervin/.config/qtile/config.py")}
                    ),
                widget.Spacer(
                    length=3),
                widget.CurrentLayoutIcon(
                    scale=0.6
                    ),
                widget.Spacer(
                    length=3),
                widget.GroupBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=12,
                    highlight_method='block',
                    block_highlight_text_color=colors_nord[4],
                    inactive=colors_nord[3],
                    active=colors_nord[4],
                    padding_y=7,
                    rounded="true"
                    ),
                widget.TaskList(
                    parse_text=no_text,
                    highlight_method='block',
                    icon_size=19,
                    border=colors_nord[3],
                    margin_y=1,
                    rounded=False,
                    ),
                widget.WidgetBox(
                    widgets=[
                        widget.Clock(
                            format='%A, %B %d - ',
                            padding=0,
                            foreground=colors_nord[6],
                            ),
                    ],
                    foreground=colors_nord[6],
                    text_closed="\uf017 ",
                    text_open="\uf017 ",
                    font='Font Awesome 5 Free Solid',
                    ),
                widget.Clock(
                    format='%H:%M',
                    padding=0,
                    foreground=colors_nord[6],
                    ),
                widget.Spacer(
                    length=bar.STRETCH
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    text="",
                    foreground=colors_nord[15]
                    ),
                widget.Volume(
                    foreground=colors_nord[15],
                     mouse_callbacks=
                    {'Button3': lambda: qtile.cmd_spawn("qpaeq")}
                    ),
                widget.TextBox(
                    text='/',
                    font='Font Awesome 5 Free Solid',
                    foreground=colors_nord[3],
                    background=colors_nord[0],
                    padding=0,
                    fontsize=39
                    ),
                widget.Battery(
                    format="{percent:2.0%}",
                    update_interval=5,
                    foreground=colors_nord[14]
                    ),
                widget.GenPollText(
                    update_interval=1,
                    foreground=colors_nord[14],
                    font="Font Awesome 5 Free Solid",
                    func=lambda:
                    subprocess.check_output("/home/ervin/.local/bin/bat_icon").decode('utf-8')
                    ),
                widget.GenPollText(
                    update_interval=1,
                    foreground=colors_nord[14],
                    font="Font Awesome 5 Free Solid",
                    fontsize=11,
                    func=lambda:
                    subprocess.check_output(
                        "/home/ervin/.local/bin/bat_charging_icon").decode('utf-8')
                    ),
                widget.TextBox(
                    text='/',
                    font='Font Awesome 5 Free Solid',
                    foreground=colors_nord[3],
                    background=colors_nord[0],
                    padding=0,
                    fontsize=39
                    ),
                widget.WidgetBox(
                    widgets=[
                        widget.TextBox(
                            text='/',
                            font='Font Awesome 5 Free Solid',
                            foreground=colors_nord[3],
                            background=colors_nord[0],
                            padding=0,
                            fontsize=39
                        ),
                        widget.TextBox(
                            font='Font Awesome 5 Free Solid',
                            text="",
                            fontsize=15,
                            foreground=colors_nord[5],
                            background=colors_nord[0],
                            ),
                        widget.GenPollText(
                            update_interval=3600,
                            foreground=colors_nord[5],
                            func=lambda: subprocess.check_output("/home/ervin/.local/bin/chkup").decode("utf-8"),
                            mouse_callbacks=
                            {'Button1':
                                lambda: qtile.cmd_spawn("alacritty -e yay")}
                            ),
                        widget.TextBox(
                            text='/',
                            font='Font Awesome 5 Free Solid',
                            foreground=colors_nord[3],
                            background=colors_nord[0],
                            padding=0,
                            fontsize=39
                            ),
                        widget.TextBox(
                            font='Font Awesome 5 Free Solid',
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
                            font='Font Awesome 5 Free Solid',
                            foreground=colors_nord[3],
                            background=colors_nord[0],
                            padding=0,
                            fontsize=39
                            ),
                        widget.Systray(
                            icon_size=19,
                            padding=2
                        ),
                        widget.TextBox(
                            text='/',
                            font='Font Awesome 5 Free Solid',
                            foreground=colors_nord[3],
                            background=colors_nord[0],
                            padding=0,
                            fontsize=39
                            ),
                        widget.TextBox(
                            text='',
                            font="Font Awesome 5 Free Solid",
                            mouse_callbacks=
                            {'Button1': lambda: reload()},
                            foreground=colors_nord[10],
                            padding=0),
                    ],
                    foreground=colors_nord[10],
                    text_closed="",
                    text_open="",
                    font='Font Awesome 5 Free Solid',
                    ),
                widget.Spacer(
                    length=5),
                widget.GenPollText(
                    update_interval=3600,
                    foreground=colors_nord[13],
                    func=lambda: subprocess.check_output("/home/ervin/.local/bin/uptime.sh").decode("utf-8")
                    ),
                widget.Spacer(
                    length=5),
                widget.TextBox(
                    text="",
                    font="Font Awesome 5 Free Solid",
                    mouse_callbacks=
                    {'Button1': lambda: qtile.cmd_spawn('nwgbar')},
                    foreground=colors_nord[11]
                    ),
                widget.Spacer(
                    length=5),
            ],
            26,
            margin=3,
            background=colors_nord[0]
        ),
    ),
]

displays = subprocess.check_output('xrandr').decode('utf-8')
display_status = displays.find('disconnected')

if display_status == -1:
    lazy.spawn("xrandr --output eDP-1 --auto --output HDMI-1 --auto --right-of eDP-1")
    screens.append(Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename="/usr/share/pixmaps/archlinux-logo.svg",
                    margin=5,
                    mouse_callbacks=
                    {'Button1': lambda: qtile.cmd_spawn("rofi -show drun -terminal alacritty -show-icons")}
                    ),
                widget.Image(
                    filename="/usr/share/icons/Papirus/64x64/apps/python.svg",
                    margin=5,
                    mouse_callbacks=
                    {'Button1': lambda: qtile.cmd_spawn("subl /home/ervin/.config/qtile/config.py")}
                    ),
                widget.Spacer(
                    length=3),
                widget.CurrentLayoutIcon(
                    scale=0.6
                    ),
                widget.Spacer(
                    length=3),
                widget.GroupBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=12,
                    highlight_method='block',
                    block_highlight_text_color=colors_nord[4],
                    inactive=colors_nord[3],
                    active=colors_nord[4],
                    padding_y=7,
                    rounded="true"
                    ),
                widget.TaskList(
                    parse_text=no_text,
                    highlight_method='block',
                    icon_size=19,
                    border=colors_nord[3],
                    margin_y=1,
                    rounded=False,
                    ),
                widget.WidgetBox(
                    widgets=[
                        widget.Clock(
                            format='%A, %B %d - ',
                            padding=0,
                            foreground=colors_nord[6],
                            ),
                    ],
                    foreground=colors_nord[6],
                    text_closed="\uf017 ",
                    text_open="\uf017 ",
                    font='Font Awesome 5 Free Solid',
                    ),
                widget.Clock(
                    format='%H:%M',
                    padding=0,
                    foreground=colors_nord[6],
                    ),
                widget.Spacer(
                    length=bar.STRETCH
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    text="",
                    foreground=colors_nord[15]
                    ),
                widget.Volume(
                    foreground=colors_nord[15],
                    mouse_callbacks=
                    {'Button3': lambda: qtile.cmd_spawn("qpaeq")}
                    ),
                widget.TextBox(
                    text='/',
                    font='Font Awesome 5 Free Solid',
                    foreground=colors_nord[3],
                    background=colors_nord[0],
                    padding=0,
                    fontsize=39
                    ),
                widget.Battery(
                    format="{percent:2.0%}",
                    update_interval=5,
                    foreground=colors_nord[14]
                    ),
                widget.GenPollText(
                    update_interval=1,
                    foreground=colors_nord[14],
                    font="Font Awesome 5 Free Solid",
                    func=lambda:
                    subprocess.check_output("/home/ervin/.local/bin/bat_icon").decode('utf-8')
                    ),
                widget.GenPollText(
                    update_interval=1,
                    foreground=colors_nord[14],
                    font="Font Awesome 5 Free Solid",
                    fontsize=11,
                    func=lambda:
                    subprocess.check_output(
                        "/home/ervin/.local/bin/bat_charging_icon").decode('utf-8')
                    ),
                widget.TextBox(
                    text='/',
                    font='Font Awesome 5 Free Solid',
                    foreground=colors_nord[3],
                    background=colors_nord[0],
                    padding=0,
                    fontsize=39
                    ),
                widget.Spacer(
                    length=5),
                widget.GenPollText(
                    update_interval=3600,
                    foreground=colors_nord[13],
                    func=lambda: subprocess.check_output("/home/ervin/.local/bin/uptime.sh").decode("utf-8")
                    ),
                widget.Spacer(
                    length=5),
                widget.TextBox(
                    text="",
                    font="Font Awesome 5 Free Solid",
                    mouse_callbacks=
                    {'Button1': lambda: qtile.cmd_spawn('nwgbar')},
                    foreground=colors_nord[11]
                    ),
                widget.Spacer(
                    length=5),
            ],
            26,
            margin=3,
            background=colors_nord[0]
            ),
        ),
    )


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.local/bin/autostart.sh')
    subprocess.call([home])

follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
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
    border_focus="#bcadf9")
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
