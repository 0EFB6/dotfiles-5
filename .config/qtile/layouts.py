from libqtile import layout
from libqtile.config import Click, Drag, Match
from libqtile.command import lazy
from keys import mod

layouts = [
    layout.Bsp(
        margin=5,
        fontsize=20,
        border_width=1,
        border_focus="#bcadf9"
        ),
    layout.Zoomy(  # !!CHECK DOCS FOR THIS ONE!!
        margin=5,
        columnwidth=150,
        fontsize=20,
        border_width=1
        ),
    layout.Max(
        margin=5,
        fontsize=20,
        ),
    layout.MonadTall(
        margin=5,
        fontsize=20,
        border_width=1,
        border_focus="#bcadf9"
        ),
    layout.MonadWide(
        margin=5,
        border_width=1,
        border_focus="#bcadf9"
        ),
    layout.Floating(
        float_rules=[
            *layout.Floating.default_float_rules,
            Match(wm_class='confirmreset'),  # gitk
            Match(wm_class='makebranch'),  # gitk
            Match(wm_class='maketag'),  # gitk
            Match(wm_class='ssh-askpass'),  # ssh-askpass
            Match(title='branchdialog'),  # gitk
            Match(title='pinentry'),  # GPG key password entry
        ],
        border_focus="#bcadf9")
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
