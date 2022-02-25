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
* `cp etc/zsh/* /etc/zsh`
* `reflector @/home/ervin/dotfiles/reflector.conf` 
* 
```
yay -S alacritty betterlockscreen conky cpupower eog exa fet.sh-git google-chrome-beta htop lightdm lightdm-slick-greeter linux-zen linux-zen-headers lxappearance-gtk3 network-manager-applet networkmanager nitrogen neovim papirus-icon-theme pulseaudio qtile-git reflector-nomirrorlist rofi ttf-font-awesome xf86-video-intel xorg zsh zsh-completions zsh-fast-syntax-highlighting
``` 
* edit /etc/pacman.conf (
`testing,core,extra,community-testing,community`
`Color,CheckSpace,VerbosePkgLists,ParallelDownloads = 5,ILoveCandy`)
* `cp .config/* /home/ervin/.config && mkdir /home/ervin/.local/bin && cp -al .local/bin/* /home/ervin/.local/bin/`
* `cp Code* /usr/share/fonts/OTF/`
* `fc-cache -f -v` 
* edit /etc/lightdm/lightdm.conf (greeter-session)
 
## Useful

* `lscpu | grep MHz`
* `fc-list | grep -i awesome`
* `fc-cache -f -v`

```
├── Code New Roman Bold Nerd Font Complete Mono.otf
├── .config
│             ├── alacritty
│             │             └── alacritty.yml
│             ├── conky
│             │             ├── conky_budgie.conf
│             │             ├── conky.conf
│             │             ├── conky_qtile.conf
│             │             ├── filesize.lua
│             │             ├── font
│             │             │             ├── build
│             │             │             ├── install
│             │             │             ├── lean-conky-config.otf
│             │             │             ├── LICENSE
│             │             │             └── TRS-Million-mod.otf
│             │             ├── LICENSE
│             │             ├── local.conf
│             │             ├── main.lua
│             │             ├── screenshot.jpg
│             │             ├── start_budgie.sh
│             │             ├── start_qtile.sh
│             │             ├── utils.lua
│             │             └── VERSION
│             ├── nwg-launchers
│             │             ├── nwgbar
│             │             │             ├── bar.json
│             │             │             └── style.css
│             │             ├── nwgdmenu
│             │             │             └── style.css
│             │             └── nwggrid
│             │                 ├── style.css
│             │                 └── terminal
│             ├── qtile
│             │             ├── config.py
│             │             ├── keys.py
│             │             ├── layouts.py
│             │             └── matches.py
│             ├── rofi
│             │             ├── config.rasi
│             │             ├── powermenu.rasi
│             │             ├── powermenu.sh
│             │             └── themes
│             │                 ├── nord.rasi
│             │                 └── powermenu_nord.rasi
│             ├── zathura
│             │             └── zathurarc
│             └── zsh
│                 ├── .zshenv
│                 └── .zshrc
├── .local
│             └── bin
│                 ├── all_disk_usage
│                 ├── anbox-shell
│                 ├── ascii-images
│                 ├── autostart
│                 ├── bandwidth-monitor
│                 ├── bat_charging_icon
│                 ├── bat_icon
│                 ├── bl_ctl
│                 ├── bl_icon
│                 ├── bl_off
│                 ├── bl_on
│                 ├── brightness_ctl
│                 ├── bw
│                 ├── change_conky_alpha
│                 ├── change_wallpaper
│                 ├── chkup
│                 ├── corona.sh
│                 ├── cpu_temp
│                 ├── display_center
│                 ├── dot-backup
│                 ├── find_hardlink
│                 ├── hard_usage
│                 ├── libinput-gestures-start
│                 ├── media_ctl
│                 ├── memory
│                 ├── netspeed
│                 ├── network_text
│                 ├── pachist
│                 ├── pkglist-backup
│                 ├── qtile_keybinds
│                 ├── qtile_key_pdf
│                 ├── rmshit.py
│                 ├── rofi-power-menu
│                 ├── spotify_left
│                 ├── spotify_pause
│                 ├── spotify_right
│                 ├── ssd_usage
│                 ├── start-spotify
│                 ├── systray
│                 ├── tray.py
│                 ├── tsize
│                 ├── uptime.sh
│                 ├── vol_ctl
│                 ├── vol_mute
│                 ├── wallpaper
│                 ├── window_icon
│                 ├── window_name
│                 ├── workdays
│                 └── x64ver
├── pkgs
├── README.md
└── reflector.conf
```
