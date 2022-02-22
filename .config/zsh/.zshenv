export DISPLAY=:0
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
export XAUTHORITY="$XDG_RUNTIME_DIR"/Xauthority
export PYTHONSTARTUP="$XDG_CONFIG_HOME"/pythonrc
export MYSQL_HISTFILE="$XDG_DATA_HOME"/mysql_history
export _JAVA_OPTIONS=-Djava.util.prefs.userRoot="$XDG_CONFIG_HOME"/java

#VARIABLES
export TERMINAL=alacritty
export EDITOR=lvim

#Aliases
alias vim="lvim"
alias nvim="lvim"
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias diff='diff --color=auto'
alias ip='ip --color=auto'
alias rm="rm -rf"
alias ls='exa --icons -H'
alias l='ls -a'
alias la='ls -a'
alias ll="ls -aghl"
alias nf="neofetch"
alias SS="sudo systemctl"
alias cat="bat"
alias q="gnome-session-quit"
alias df="df -h -x tmpfs -x devtmpfs -x squashfs"
alias p="sudo pacman"
alias gp="git add .; git commit -m 'commit'; git push"
alias o="xdg-open"
alias nvidia-settings="nvidia-settings --config="$XDG_CONFIG_HOME"/nvidia/settings"
alias wget='wget --hsts-file="$XDG_CACHE_HOME/wget-hsts"'
alias sway="sway --my-next-gpu-wont-be-nvidia"
alias b="$HOME/.local/bin/"
alias c="$HOME/.config"
alias d="$HOME/www/src/mine/dotfiles"
alias sa="adb forward tcp:8022 tcp:8022 && adb forward tcp:8080 tcp:8080 && ssh localhost -p 8022 -i ~/.ssh/id_rsa_android"
alias neo="neo -D"
alias neo-ru="neo --color=red --charset=cyrillic -m 'IN SOVIET RUSSIA, COMPUTER PROGRAMS YOU'" 
alias tty-clock="tty-clock -c -C 7 -f '%a, %d %b'"

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
