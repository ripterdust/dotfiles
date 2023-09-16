from libqtile import bar, layout, hook
from libqtile.config import Click, Drag, Key, Screen, Match
from libqtile.lazy import lazy
from modules.groups import groups, get_group_key
from modules.keys import keybindings
from modules.bar import getWidgets, size, margin
from modules.colors import nord_fox, dracula

import subprocess
import os


def init_colors():
    return [["#282c34", "#282c34"],
            ["#1c1f24", "#1c1f24"],
            ["#dfdfdf", "#dfdfdf"],
            ["#ff6c6b", "#ff6c6b"],
            ["#98be65", "#98be65"],
            ["#da8548", "#da8548"],
            ["#51afef", "#51afef"],
            ["#c678dd", "#c678dd"],
            ["#46d9ff", "#46d9ff"],
            ["#a9a1e1", "#a9a1e1"]]


colors = init_colors()

mod = "mod4"
terminal = "alacritty"

keys = [
    *keybindings
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                str(get_group_key(i.name)),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                str(get_group_key(i.name)),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=[
                   "#d75f5f", "#8f3d3d"], border_width=0, margin=7, border_on_single=True),
    layout.Max(margin=7),
]

widget_defaults = dict(
    font="Fira Code Nerd Font",
    fontsize=12,
    padding=6,
    background=dracula['bg'],
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        # top=bar.Bar([*getWidgets()], size=size, margin=margin),
    ),
    Screen(
        # top=bar.Bar([*getWidgets()], size=size, margin=margin),
    )
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = ''
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "Bryan"


commands = [
    'feh --bg-fill ~/.config/qtile/wallpaper.jpg',
    'picom --config ~/.config/picom/picom.conf &',
    'nm-applet &',
    'setxkbmap latam',
    "/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &",
    "polybar first &",
    "polybar second &",
]

for command in commands:
    os.system(command)

# Copyright - Bryan Arévalo 2023
