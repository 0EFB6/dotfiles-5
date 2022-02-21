# dotfiles

## Install

* ping archlinux.org
* timedatectl set-ntp true
* create partition with fdisk : 500M for boot 20G for root the rest for home (change type to 1 for boot to UEFI)
* mkfs.fat -F32 for boot and mkfs.ext4 for root and home
* mount /mnt on root fs and /mnt/home (mkdir) on home fs
* cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup
* pacman -Sy pacman-mirrorlist
* rankmirrors -n 6 /etc/pacman.d/mirrorlist.backup > /etc/pacman.d/mirrorlist
* pacstrap /mnt base base-devel vim git
* genfstab -U -p /mnt >> /mnt/etc/fstab
* arch-chroot /mnt

## Post-Install

* useradd -m -g wheel ervin 
* passwd ervin 
* visudo
* cd /home/ervin
* git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si --noconfirm 
* yay -S cpupower xf86-video-intel nvim zsh linux-zen linux-zen-headers xorg-server xorg-xinit lightdm lightdm-slick-greeter qtile exa
* git clone https://github.com/ervinpopescu/dotfiles && cd dotfiles
* cp .config/* /home/ervin/.config && mkdir /home/ervin/.local/bin && cp -al .local/bin/* /home/ervin/.local/bin/
* edit /etc/lightdm/lightdm.conf (greeter-session)
## Useful

* lscpu | grep MHz
* fc-list | grep -i awesome
* fc-cache -f -v
