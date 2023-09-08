from libqtile.bar import Bar
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.spacer import Spacer
from libqtile.widget.clock import Clock
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.battery import Battery
from libqtile.widget.quick_exit import QuickExit
from libqtile.widget.backlight import Backlight
from libqtile.widget.chord import Chord
from libqtile.widget.notify import Notify
from libqtile.widget.statusnotifier import StatusNotifier
from libqtile.widget.check_updates import CheckUpdates

from libqtile import widget

from qtile_extras import widget

from .unicodes import right_arrow, left_arrow
from .colors import nord_fox, gruvbox

BAR_HEIGHT = 28

notifications = Notify()
windows = GroupBox(
    disable_drag=True,
    active=nord_fox['red'],
    inactive=nord_fox['black'],
    highlight_method='line',
    block_highlight_text_color=nord_fox['fg_gutter'],
    borderwidth=0,
    highlight_color=nord_fox['bg'],
    background=nord_fox['bg'],
    spacing=2

)


def getWidgets():
    statusWidgets = [
        windows,
        right_arrow(nord_fox['red'], nord_fox['bg']),
        CurrentLayout(
            background=nord_fox['red'],
            foreground=nord_fox['white'],
            margin=10,
        ),
        right_arrow(nord_fox['fg_gutter'], nord_fox['red']),
        WindowCount(
            text_format='󰹑 {num}',
            background=nord_fox['fg_gutter'],
            foreground=nord_fox['white'],
            show_zero=True,
        ),
        right_arrow(nord_fox['bg'], nord_fox['fg_gutter']),
        WindowName(
            background=nord_fox['bg'],
            foreground=nord_fox['fg'],
        ),
        notifications,
        Chord(chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
            name_transform=lambda name: name.upper()),
        left_arrow(nord_fox['bg'], nord_fox['orange']),
        Battery(
            background=nord_fox['orange'],
            format='Battery \uf240  {percent:2.0%}'
        ),
        left_arrow(nord_fox['orange'], gruvbox['yellow']),
        widget.PulseVolume(background=gruvbox['yellow']),
        left_arrow(gruvbox['yellow'], gruvbox['blue']),
        CheckUpdates(
            background=gruvbox['blue'],
            distro="Arch",
            no_update_string="No updates",
            display_format="Updates: {updates}",
        ),
        left_arrow(gruvbox['blue'], gruvbox['yellow']),
        widget.KeyboardLayout(
            fmt='Keyboard: {}',
            padding=5,
            background=gruvbox['yellow'],
            foreground=nord_fox['black'],
            configured_keyboards=['latam']
        ),
        left_arrow(gruvbox['yellow'], nord_fox['blue']),
        Clock(
            background=nord_fox['blue'],
            foreground=nord_fox['black'],
            format='\uf017 %a %I:%M %p %d/%m/%Y'
        ),
        left_arrow(nord_fox['blue'], nord_fox['red']),
        QuickExit(default_text="󰤆", countdown_format="{}",
                  fontsize=17, background=nord_fox['red']),
        Spacer(length=5, background=nord_fox['red']),


    ]

    return statusWidgets


size = BAR_HEIGHT
margin = 5
