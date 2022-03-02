# dotfiles

## Install

* `ping archlinux.org`
* `timedatectl set-ntp true`
* create partition with `fdisk` : 500M for boot 20G for root the rest for home (change type to 1 for boot to UEFI)
* `mkfs.fat -F32` for boot and `mkfs.ext4` for root and home
* `mount` /mnt on root fs and /mnt/home (mkdir) on home fs
* `cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup`
* `pacman -Sy pacman-mirrorlist`
* `rankmirrors -n 6 /etc/pacman.d/mirrorlist.backup > /etc/pacman.d/mirrorlist`
* `pacstrap /mnt base base-devel vim git`
* `genfstab -U -p /mnt >> /mnt/etc/fstab`
* `arch-chroot /mnt`

## Post-Install

* `echo "arch" > /etc/hostname`
* `echo -e "127.0.0.1 localhost\n::1 localhost" > /etc/hosts`
* `useradd -m -g wheel ervin` 
* `passwd ervin` 
* `EDITOR=vim visudo`
* `cd /home/ervin`
* `git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si --noconfirm`
* `git clone https://github.com/ervinpopescu/dotfiles && cd dotfiles`
* `reflector @/home/ervin/dotfiles/reflector.conf` 
* 
```
yay -S alacritty betterlockscreen conky cpupower eog exa fet.sh-git google-chrome-beta htop lightdm lightdm-slick-greeter linux-zen linux-zen-headers lxappearance-gtk3 network-manager-applet networkmanager nitrogen neovim papirus-icon-theme pulseaudio qtile-git reflector-nomirrorlist rofi ttf-font-awesome xf86-video-intel xorg zsh zsh-completions zsh-fast-syntax-highlighting
``` 
* edit /etc/pacman.conf (

`testing,core,extra,community-testing,community`
`Color,CheckSpace,VerbosePkgLists,ParallelDownloads = 5,ILoveCandy`)
* `cp etc/zsh/* /etc/zsh`
* `cp .config/* /home/ervin/.config && mkdir /home/ervin/.local/bin && cp -al .local/bin/* /home/ervin/.local/bin/`
* `cp Code* /usr/share/fonts/OTF/`
* `fc-cache -f -v` 
* edit /etc/lightdm/lightdm.conf (greeter-session)
 
## Useful

* `lscpu | grep MHz`
* `fc-list | grep -i awesome`
* `fc-cache -f -v`

<!DOCTYPE html>
<html>
<body>
	<h1>Directory Tree</h1><p>
	<a href=""></a><br>
	├── <a href="/Code%20New%20Roman%20Bold%20Nerd%20Font%20Complete%20Mono.otf">Code New Roman Bold Nerd Font Complete Mono.otf</a><br>
	├── <a href="/.config/">.config</a><br>
	│   ├── <a href="/.config/alacritty/">alacritty</a><br>
	│   │   └── <a href="/.config/alacritty/alacritty.yml">alacritty.yml</a><br>
	│   ├── <a href="/.config/conky/">conky</a><br>
	│   │   ├── <a href="/.config/conky/conky_budgie.conf">conky_budgie.conf</a><br>
	│   │   ├── <a href="/.config/conky/conky.conf">conky.conf</a><br>
	│   │   ├── <a href="/.config/conky/conky_qtile.conf">conky_qtile.conf</a><br>
	│   │   ├── <a href="/.config/conky/filesize.lua">filesize.lua</a><br>
	│   │   ├── <a href="/.config/conky/font/">font</a><br>
	│   │   │   ├── <a href="/.config/conky/font/build">build</a><br>
	│   │   │   ├── <a href="/.config/conky/font/install">install</a><br>
	│   │   │   ├── <a href="/.config/conky/font/lean-conky-config.otf">lean-conky-config.otf</a><br>
	│   │   │   ├── <a href="/.config/conky/font/LICENSE">LICENSE</a><br>
	│   │   │   └── <a href="/.config/conky/font/TRS-Million-mod.otf">TRS-Million-mod.otf</a><br>
	│   │   ├── <a href="/.config/conky/local.conf">local.conf</a><br>
	│   │   ├── <a href="/.config/conky/main.lua">main.lua</a><br>
	│   │   ├── <a href="/.config/conky/start_budgie.sh">start_budgie.sh</a><br>
	│   │   ├── <a href="/.config/conky/start_qtile.sh">start_qtile.sh</a><br>
	│   │   └── <a href="/.config/conky/utils.lua">utils.lua</a><br>
	│   ├── <a href="/.config/nwg-launchers/">nwg-launchers</a><br>
	│   │   ├── <a href="/.config/nwg-launchers/nwgbar/">nwgbar</a><br>
	│   │   │   ├── <a href="/.config/nwg-launchers/nwgbar/bar.json">bar.json</a><br>
	│   │   │   └── <a href="/.config/nwg-launchers/nwgbar/style.css">style.css</a><br>
	│   │   ├── <a href="/.config/nwg-launchers/nwgdmenu/">nwgdmenu</a><br>
	│   │   │   └── <a href="/.config/nwg-launchers/nwgdmenu/style.css">style.css</a><br>
	│   │   └── <a href="/.config/nwg-launchers/nwggrid/">nwggrid</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/nwg-launchers/nwggrid/style.css">style.css</a><br>
	│   │   &nbsp;&nbsp;&nbsp; └── <a href="/.config/nwg-launchers/nwggrid/terminal">terminal</a><br>
	│   ├── <a href="/.config/qtile/">qtile</a><br>
	│   │   ├── <a href="/.config/qtile/config.py">config.py</a><br>
	│   │   └── <a href="/.config/qtile/modules/">modules</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/get_screens.py">get_screens.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/groups.py">groups.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/__init__.py">__init__.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/keys.py">keys.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/layouts.py">layouts.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/matches.py">matches.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/mouse.py">mouse.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/qtile/modules/settings.py">settings.py</a><br>
	│   │   &nbsp;&nbsp;&nbsp; └── <a href="/.config/qtile/modules/widgets.py">widgets.py</a><br>
	│   ├── <a href="/.config/rofi/">rofi</a><br>
	│   │   ├── <a href="/.config/rofi/config.rasi">config.rasi</a><br>
	│   │   ├── <a href="/.config/rofi/powermenu.rasi">powermenu.rasi</a><br>
	│   │   ├── <a href="/.config/rofi/powermenu.sh">powermenu.sh</a><br>
	│   │   └── <a href="/.config/rofi/themes/">themes</a><br>
	│   │   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/rofi/themes/nord.rasi">nord.rasi</a><br>
	│   │   &nbsp;&nbsp;&nbsp; └── <a href="/.config/rofi/themes/powermenu_nord.rasi">powermenu_nord.rasi</a><br>
	│   ├── <a href="/.config/zathura/">zathura</a><br>
	│   │   └── <a href="/.config/zathura/zathurarc">zathurarc</a><br>
	│   └── <a href="/.config/zsh/">zsh</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.config/zsh/.zshenv">.zshenv</a><br>
	│   &nbsp;&nbsp;&nbsp; └── <a href="/.config/zsh/.zshrc">.zshrc</a><br>
	├── <a href="/etc/">etc</a><br>
	│   ├── <a href="/etc/zprofile">zprofile</a><br>
	│   └── <a href="/etc/zshenv">zshenv</a><br>
	├── <a href="/.gitignore">.gitignore</a><br>
	├── <a href="/.local/">.local</a><br>
	│   └── <a href="/.local/bin/">bin</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/all_disk_usage">all_disk_usage</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/anbox-shell">anbox-shell</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/ascii-images">ascii-images</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/autostart">autostart</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bandwidth-monitor">bandwidth-monitor</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bat_charging_icon">bat_charging_icon</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bat_icon">bat_icon</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bl_ctl">bl_ctl</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bl_icon">bl_icon</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bl_off">bl_off</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bl_on">bl_on</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/brightness_ctl">brightness_ctl</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/bw">bw</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/change_conky_alpha">change_conky_alpha</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/change_wallpaper">change_wallpaper</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/chkup">chkup</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/corona.sh">corona.sh</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/cpu_temp">cpu_temp</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/display_center">display_center</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/dot-backup">dot-backup</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/find_hardlink">find_hardlink</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/hard_usage">hard_usage</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/libinput-gestures-start">libinput-gestures-start</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/media_ctl">media_ctl</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/memory">memory</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/netspeed">netspeed</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/network_text">network_text</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/pachist">pachist</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/pkglist-backup">pkglist-backup</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/qtile_keybinds">qtile_keybinds</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/qtile_key_pdf">qtile_key_pdf</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/rmshit.py">rmshit.py</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/rofi-power-menu">rofi-power-menu</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/spotify-notification">spotify-notification</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/ssd_usage">ssd_usage</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/start-spotify">start-spotify</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/suspend-off">suspend-off</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/suspend-on">suspend-on</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/systray">systray</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/tray.py">tray.py</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/tsize">tsize</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/uptime.sh">uptime.sh</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/vol_ctl">vol_ctl</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/vol_mute">vol_mute</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/wallpaper">wallpaper</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/window_icon">window_icon</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/window_name">window_name</a><br>
	│   &nbsp;&nbsp;&nbsp; ├── <a href="/.local/bin/workdays">workdays</a><br>
	│   &nbsp;&nbsp;&nbsp; └── <a href="/.local/bin/x64ver">x64ver</a><br>
	├── <a href="/pkgs">pkgs</a><br>
	├── <a href="/qtile.log">qtile.log</a><br>
	├── <a href="/README.md">README.md</a><br>
	├── <a href="/reflector.conf">reflector.conf</a><br>
	└── <a href="/test">test</a><br>
<br><br><p>

17 directories, 96 files

</p>
	<hr>
	<p class="VERSION">
		 tree v2.0.2 © 1996 - 2022 by Steve Baker and Thomas Moore <br>
		 HTML output hacked and copyleft © 1998 by Francesc Rocher <br>
		 JSON output hacked and copyleft © 2014 by Florian Sesser <br>
		 Charsets / OS/2 support © 2001 by Kyosuke Tokoro
	</p>
</body>
</html>
