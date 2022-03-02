import psutil

from libqtile import hook
from libqtile.config import (
    DropDown,
    Group,
    ScratchPad,
    Key
)
from libqtile.lazy import lazy

from .settings import (
    group_names,
    group_layouts,
    group_labels
)
from .keys import keys, mod, terminal
from .matches import d


groups = []

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
    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)


@hook.subscribe.client_new
def _swallow(window):
    pid = window.window.get_net_wm_pid()
    ppid = psutil.Process(pid).ppid()
    cpids = {c.window.get_net_wm_pid(): wid for wid,
             c in window.qtile.windows_map.items()}
    for i in range(5):
        if not ppid:
            return
        if ppid in cpids:
            parent = window.qtile.windows_map.get(cpids[ppid])
            parent.minimized = True
            window.parent = parent
            return
        ppid = psutil.Process(ppid).ppid()


@hook.subscribe.client_killed
def _unswallow(window):
    if hasattr(window, 'parent'):
        window.parent.minimized = False


for i, name in enumerate(group_names, 1):
    keys.extend([
        Key([mod], str(i), lazy.group[name].toscreen()),
        Key([mod, 'shift'], str(i), lazy.window.togroup(name))])
