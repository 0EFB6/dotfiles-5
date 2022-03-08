# export DISPLAY=:0
export PATH=/home/ervin/www/src/cloned/gnirehtet:/home/ervin/.local/bin:/home/ervin/.local/share/gem/ruby/3.0.0/bin:$PATH

#XDG Base Directory specification
export XDG_STATE_HOME="$HOME"/.local/state
export XDG_CONFIG_HOME="$HOME"/.config
export XDG_DATA_HOME=/home/ervin/.local/share
export XDG_CACHE_HOME=/home/ervin/.cache
export CARGO_HOME="$XDG_DATA_HOME"/cargo
export GTK2_RC_FILES="$XDG_CONFIG_HOME"/gtk-2.0/gtkrc
export OCTAVE_HISTFILE="$XDG_CACHE_HOME"/octave-hsts
export OCTAVE_SITE_INITFILE="$XDG_CONFIG_HOME"/octave/octaverc
export GNUPGHOME="$XDG_DATA_HOME"/gnupg
export WGETRC="$XDG_CONFIG_HOME"/wgetrc
export XINITRC="$XDG_CONFIG_HOME"/X11/xinitrc
export HISTFILE="$XDG_STATE_HOME"/zsh/history
export PYTHONSTARTUP="$XDG_CONFIG_HOME"/pythonrc
export MYSQL_HISTFILE="$XDG_DATA_HOME"/mysql_history
export _JAVA_OPTIONS=-Djava.util.prefs.userRoot="$XDG_CONFIG_HOME"/java
export __NV_PRIME_RENDER_OFFLOAD=1
export __GLX_VENDOR_LIBRARY_NAME="nvidia"
export __VK_LAYER_NV_optimus="NVIDIA_only"


#VARIABLES
export TERMINAL=alacritty
export EDITOR=lvim
export BEEP=/usr/share/sounds/gnome/default/alerts/sonar.ogg

#Aliases
alias cl="clear; sleep 0.5; la"
alias copy="xclip -selection clipboard"
alias beep='paplay $BEEP'
alias b="$HOME/.local/bin/"
alias c="$HOME/.config"
alias d="$HOME/www/src/mine/dotfiles"
alias cat="bat"
alias df="df -h -x tmpfs -x devtmpfs -x squashfs"
alias diff='diff --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias gp="git add .; git commit -m 'commit'; git push"
alias grep='grep --color=auto'
alias ip='ip --color=auto'
alias ls='exa --color=auto --icons -H'
alias l='ls -a'
alias la='ls -a'
alias ll="ls -aghl"
alias neo-ru="neo --color=red --charset=cyrillic -m 'IN SOVIET RUSSIA, COMPUTER PROGRAMS YOU'" 
alias neo="neo -D"
alias nf="neofetch"
alias nvidia-settings="nvidia-settings --config="$XDG_CONFIG_HOME"/nvidia/settings"
alias nvim="lvim"
alias o="xdg-open"
alias p="sudo pacman"
alias q="gnome-session-quit"
alias rm="rm -rf"
alias sa="adb forward tcp:8022 tcp:8022 && adb forward tcp:8080 tcp:8080 && ssh localhost -p 8022 -i ~/.ssh/id_rsa_android"
alias SS="sudo systemctl"
alias sway="sway --my-next-gpu-wont-be-nvidia"
alias tty-clock="tty-clock -c -C 7 -f '%a, %d %b'"
alias vim="lvim"
alias wget='wget --hsts-file="$XDG_CACHE_HOME/wget-hsts"'
alias feh="feh -d --edit --scale-down --auto-zoom"

#checking for tty or not
if [[ "$(tty | sed -e 's:/dev/::;s/[0-9]//')" == "tty" ]]
then
	alias ls="exa -H"
	alias nvim="nvim"
	alias vim="nvim"
  echo -en "\e[?25h"
else
	xhost si:localuser:root > /dev/null
fi

if [ -z "${DISPLAY}" ] && [ "$(tty)" = "/dev/tty8" ]; then
  startx /bin/zathura
fi

export b="$HOME/.local/bin"
export c="$XDG_CONFIG_HOME"
export d="$HOME/www/src/mine/dotfiles"

fet.sh
