from libqtile import hook
from libqtile.config import (
    DropDown,
    Group,
    ScratchPad,
    Key
)
from libqtile.lazy import lazy

from .keys import keys
from ..utils.settings import mod, terminal

groups = []

group_names = 'coding www social settings etc media'.split()
group_labels = ["", "", "", "", "", ""]
group_layouts = ["bsp", "max", "zoomy", "bsp", "bsp", "monadthreecol"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i],
            label=group_labels[i]
        ))

groups.append(
    ScratchPad(
        "scratchpad",
        [DropDown("term", terminal, opacity=0.8)]))


@hook.subscribe.client_new
def assign_app_group(client):

    from .matches import d
    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)

for i, name in enumerate(group_names, 1):
    keys.extend([
        Key([mod], str(i), lazy.group[name].toscreen()),
        Key([mod, 'shift'], str(i), lazy.window.togroup(name))])
