from libqtile import hook
from libqtile.config import (
    DropDown,
    Group,
    ScratchPad,
    Key
)
from libqtile.command import lazy
from keys import keys, mod, terminal

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
        "google-chrome-beta",
        "Google-chrome-beta",
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
