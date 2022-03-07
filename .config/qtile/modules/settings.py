############
# SETTINGS #
############

# Keys
mod = "mod4"
alt = "mod1"
terminal = "alacritty"

# Groups
group_names = 'coding www social etc settings media'.split()
group_labels = ["", "", "", "", "", ""]
group_layouts = ["monadwide", "max", "max", "bsp", "bsp", "monadthreecol"]

# Widgets
colors = ["#2e3440",   # 0
          "#3b4252",   # 1
          "#434c5e",   # 2
          "#4c566a",   # 3
          "#d8dee9",   # 4
          "#e5e9f0",   # 5
          "#eceff4",   # 6
          "#8fbcbb",   # 7
          "#88c0d0",   # 8
          "#81a1c1",   # 9
          "#5e81ac",   # 10
          "#bf616a",   # 11
          "#d08770",   # 12
          "#ebcb8b",   # 13
          "#a3be8c",   # 14
          "#b48ead",   # 15
          ]

widget_defaults = dict(
    font="CodeNewRoman Nerd Font Mono Bold",
    fontsize=15,
    padding=3,

)

extension_defaults = widget_defaults.copy()
