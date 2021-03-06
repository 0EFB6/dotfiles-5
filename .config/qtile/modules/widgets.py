import re
import subprocess

from libqtile import bar, qtile, widget, hook
from libqtile.lazy import lazy
from .settings import colors


def no_text(text):
    return ''


def reload():
    qtile.cmd_reload_config()
    qtile.cmd_spawn('/home/ervin/.local/bin/change_wallpaper')


curl = ["curl", "-s", 'wttr.in/?format="%c+%t"']


@hook.subscribe.focus_change
def weather_color():
    weather = subprocess.check_output(
        ["curl", "-s", 'wttr.in/?format="%c+%t"']).decode("utf-8")
    degrees = re.findall(
        r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', weather)
    if degrees[0][0] == "+":
        color = colors[13]
    else:
        color = colors[7]
    return color


def primary_widgets():
    return [
        widget.Image(
            filename="/home/ervin/.config/qtile/logo.svg",
            margin_y=2,
            margin_x=1,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                "rofi -show drun -terminal alacritty -show-icons")}
        ),
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
            foreground=colors[3],
            background=colors[0],
            padding=0,
            fontsize=35
        ),
        widget.GroupBox(
            font='Font Awesome 6 Free Solid',
            fontsize=12,
            highlight_method='block',
            block_highlight_text_color=colors[4],
            inactive=colors[3],
            active=colors[4],
            padding_y=7,
            rounded="true"
        ),
        widget.TextBox(
            text='/',
            foreground=colors[3],
            background=colors[0],
            padding=0,
            fontsize=35
        ),
        widget.CurrentLayout(),
        widget.TextBox(
            text='/',
            foreground=colors[3],
            background=colors[0],
            padding=0,
            fontsize=35
        ),
        widget.TaskList(
            parse_text=no_text,
            # highlight_method='block',
            icon_size=19,
            border=colors[3],
            rounded=False,
            padding=1
        ),
        widget.WidgetBox(
            widgets=[
                widget.Clock(
                    format='%A, %B %d - ',
                    padding=0,
                    foreground=colors[6],
                    fontsize=15
                ),
            ],
            foreground=colors[6],
            text_closed="\uf017 ".encode("utf-8"),
            text_open="\uf017 ".encode("utf-8"),
            font='Font Awesome 6 Free Solid',
            fontsize=15
        ),
        widget.Clock(
            format='%H:%M',
            padding=0,
            foreground=colors[6],
            fontsize=15
        ),
        widget.Spacer(
            length=bar.STRETCH
        ),
        # widget.TextBox(
        #     font='Font Awesome 6 Free Solid',
        #     text="???",
        #     foreground=colors[15]
        # ),
        # widget.Volume(
        #     foreground=colors[15],
        #     mouse_callbacks={
        #         'Button3': lambda: qtile.cmd_spawn("pavucontrol")}
        # ),
        # widget.TextBox(
        #     text='/',
        #     foreground=colors[3],
        #     background=colors[0],
        #     padding=0,
        #     fontsize=35
        # ),
        widget.TextBox(
            font='Font Awesome 6 Free Solid',
            text="???",
            fontsize=15,
            foreground=colors[14],
            background=colors[0],
        ),
        widget.KeyboardLayout(
            configured_keyboards=["us", "ro std"],
            display_map={'us': 'us', 'ro std': 'ro'},
            foreground=colors[14],
            background=colors[0],
        ),
        widget.TextBox(
            text='/',
            foreground=colors[3],
            background=colors[0],
            padding=0,
            fontsize=35
        ),
        widget.TextBox(
            font='Font Awesome 6 Free Solid',
            text="???",
            fontsize=15,
            foreground=colors[5],
            background=colors[0],
        ),
        widget.GenPollText(
            update_interval=3600,
            foreground=colors[5],
            func=lambda: subprocess.check_output(
                "/home/ervin/.local/bin/chkup"
            ).decode("utf-8"),
            mouse_callbacks={'Button1':
                             lambda: qtile.cmd_spawn(
                                 "alacritty -e yay"
                             )}
        ),
        widget.TextBox(
            text='/',
            foreground=colors[3],
            background=colors[0],
            padding=0,
            fontsize=35
        ),
        # widget.TextBox(
        #     font='Font Awesome 6 Free Solid',
        #     text="???",
        #     padding=2,
        #     foreground=colors[13]
        # ),
        # widget.Spacer(
        #     length=3),
        # widget.Backlight(
        #     padding=0,
        #     backlight_name="intel_backlight",
        #     foreground=colors[13]
        # ),
        # widget.TextBox(
        #     text='/',
        #     foreground=colors[3],
        #     background=colors[0],
        #     padding=0,
        #     fontsize=35
        # ),
        widget.Systray(
            icon_size=16,
            padding=3,
            margin_y=10
        ),
        widget.TextBox(
            text='/',
            foreground=colors[3],
            background=colors[0],
            padding=0,
            fontsize=35
        ),
        widget.Battery(
            format="{percent:2.0%}",
            update_interval=5,
            foreground=colors[14]
        ),
        widget.GenPollText(
            update_interval=1,
            padding=1,
            foreground=colors[14],
            font="Font Awesome 6 Free Solid",
            func=lambda:
            subprocess.check_output(
                "/home/ervin/.local/bin/bat_icon"
            ).decode('utf-8')
        ),
        widget.GenPollText(
            update_interval=1,
            padding=0,
            foreground=colors[14],
            font="Font Awesome 6 Free Solid",
            fontsize=11,
            func=lambda:
            subprocess.check_output(
                "/home/ervin/.local/bin/bat_charging_icon"
            ).decode('utf-8')),
        widget.TextBox(
            text='/',
            foreground=colors[3],
            background=colors[0],
            padding=0,
            fontsize=35
        ),
        widget.GenPollText(
            update_interval=900,
            foreground=weather_color(),
            # font="Font Awesome 6 Free Solid",
            func=lambda: subprocess.check_output(curl).decode(
                "utf-8").strip('"').replace(" ", "")
        ),
        widget.TextBox(
            text='/',
            foreground=colors[3],
            background=colors[0],
            padding=0,
            fontsize=35
        ),
        widget.TextBox(
            text='???',
            font="Font Awesome 6 Free Solid",
            mouse_callbacks={'Button1': lambda: reload()},
            foreground=colors[10],
            padding=0),
        widget.Spacer(
            length=5),
        widget.GenPollText(
            update_interval=3600,
            foreground=colors[13],
            func=lambda: subprocess.check_output(
                "/home/ervin/.local/bin/uptime.sh").decode("utf-8")
        ),
        widget.Spacer(
            length=5),
        widget.TextBox(
            text="???",
            font="Font Awesome 6 Free Solid",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('nwgbar')},
            foreground=colors[11]
        ),
        widget.Spacer(
            length=5),
    ]


def secondary_widgets():
    return [
        widget.Image(
            filename="/usr/share/pixmaps/archlinux-logo.png",
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
            foreground=colors[3],
            background=colors[0],
            padding=0,
            fontsize=35
        ),
        widget.GroupBox(
            font='Font Awesome 6 Free Solid',
            fontsize=12,
            highlight_method='block',
            block_highlight_text_color=colors[4],
            inactive=colors[3],
            active=colors[4],
            padding_y=7,
            rounded="true"
        ),
        widget.TextBox(
            text='/',
            foreground=colors[3],
            background=colors[0],
            padding=0,
            fontsize=35
        ),
        # widget.CurrentLayoutIcon(
        #     scale=0.6
        #     ),
        widget.CurrentLayout(),
        widget.TextBox(
            text='/',
            foreground=colors[3],
            background=colors[0],
            padding=0,
            fontsize=35
        ),
        widget.TaskList(
            parse_text=no_text,
            highlight_method='block',
            icon_size=19,
            border=colors[3],
            margin=5,
            rounded=False,
            padding_x=3
        ),
        widget.WidgetBox(
            widgets=[
                widget.Clock(
                    format='%A, %B %d - ',
                    padding=0,
                    foreground=colors[6],
                    fontsize=15
                ),
            ],
            foreground=colors[6],
            text_closed="\uf017 ",
            text_open="\uf017 ",
            font='Font Awesome 6 Free Solid',
            fontsize=15
        ),
        widget.Clock(
            format='%H:%M',
            padding=0,
            foreground=colors[6],
            fontsize=15
        ),
        widget.Spacer(
            length=bar.STRETCH
        ),
        widget.TextBox(
            font='Font Awesome 6 Free Solid',
            text="???",
            fontsize=15,
            foreground=colors[5],
            background=colors[0],
        ),
        widget.GenPollText(
            update_interval=3600,
            foreground=colors[5],
            func=lambda: subprocess.check_output(
                "/home/ervin/.local/bin/chkup"
            ).decode("utf-8"),
            mouse_callbacks={'Button1':
                             lambda: qtile.cmd_spawn("alacritty -e yay")}
        ),
        widget.TextBox(
            text='/',
            foreground=colors[3],
            background=colors[0],
            padding=0,
            fontsize=35
        ),
        widget.TextBox(
            font='Font Awesome 6 Free Solid',
            text="???",
            padding=2,
            foreground=colors[13]
        ),
        widget.Spacer(
            length=3),
        widget.Backlight(
            padding=0,
            backlight_name="intel_backlight",
            foreground=colors[13]
        ),
        widget.TextBox(
            text='/',
            foreground=colors[3],
            background=colors[0],
            padding=0,
            fontsize=35
        ),
        widget.TextBox(
            text='???',
            font="Font Awesome 6 Free Solid",
            mouse_callbacks={'Button1': lambda: reload()},
            foreground=colors[10],
            padding=0),
        widget.Spacer(
            length=5),
        widget.GenPollText(
            update_interval=3600,
            foreground=colors[13],
            func=lambda: subprocess.check_output(
                "/home/ervin/.local/bin/uptime.sh").decode("utf-8")
        ),
        widget.Spacer(
            length=5),
        widget.TextBox(
            text="???",
            font="Font Awesome 6 Free Solid",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('nwgbar')},
            foreground=colors[11]
        ),
        widget.Spacer(
            length=5),
    ]
