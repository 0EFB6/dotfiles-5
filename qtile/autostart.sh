#!/bin/sh

/usr/bin/pkill -KILL wallpaper.sh
/usr/bin/pkill -KILL sleep
/usr/bin/blueman-applet &
/usr/bin/nm-applet &
/usr/bin/pasystray &
/home/ervin/.scripts/wallpaper.sh &
/usr/bin/picom -f --blur-method dual_kawase --blur-strength 1 --corner-radius 5 &
# /home/ervin/.config/conky/lean-conky-config/start_qtile.sh -n &
/usr/bin/flameshot &
/usr/bin/xss-lock -- betterlockscreen -l dimblur &
gnome-keyring-daemon --start
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# nwggrid-server &
