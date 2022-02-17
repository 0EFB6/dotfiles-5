#!/bin/sh

gnome-keyring-daemon --start
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
pkill -KILL wallpaper.sh
pkill -KILL sleep
/home/ervin/.local/bin/wallpaper.sh &
blueman-applet &
nm-applet & disown
flameshot &
xset s 600 &
xss-lock -- betterlockscreen -l dimblur &
# /home/ervin/.config/conky/lean-conky-config/start_qtile.sh -n &
picom -f --blur-method dual_kawase --blur-strength 1 --corner-radius 5 &
albert &
