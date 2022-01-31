#!/bin/env bash

rofi -show power-menu \
     -modi "power-menu:/home/ervin/.bin/rofi-power-menu --choices=suspend/logout/reboot/shutdown --confirm=reboot/shutdown" \
     -config /home/ervin/.config/rofi/powermenu.rasi