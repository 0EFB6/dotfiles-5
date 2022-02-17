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
