from libqtile import layout
from libqtile.config import Match

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
        border_focus="#bcadf9",
        max_ratio=0.9
    ),
    layout.MonadThreeCol(
        margin=5,
        border_width=0,
        ratio=0.33,
        max_ratio=0.95
    ),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ],
    border_width=0)
