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
from libqtile.widget.pulse_volume import PulseVolume
from libqtile.widget.backlight import Backlight
from libqtile.widget.chord import Chord
from libqtile.widget.notify import Notify
from libqtile.widget.statusnotifier import StatusNotifier
from qtile_extras import widget

from .unicodes import left_half_circle, right_arrow, left_arrow, right_half_circle
from .colors import nord_fox, gruvbox

BAR_HEIGHT = 28


def getWidgets():
    statusWidgets = [
        GroupBox(
            disable_drag=True,
            active=nord_fox['red'],
            inactive=nord_fox['black'],
            highlight_method='line',
            block_highlight_text_color=nord_fox['fg_gutter'],
            borderwidth=0,
            highlight_color=nord_fox['bg'],
            background=nord_fox['bg'],
            spacing=2

        ),
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
        Notify(
        ),
        left_arrow(nord_fox['bg'], nord_fox['black']),
        CPU(
            format=' {freq_current}GHz {load_percent}%',
            background=nord_fox['black'],
            foreground=nord_fox['white']
        ),
        Memory(
            format='󱦟{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
            background=nord_fox['black'],
            foreground=nord_fox['cyan']
        ),
        Chord(chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
            name_transform=lambda name: name.upper()),

        left_arrow(nord_fox['black'], nord_fox['blue']),
        StatusNotifier(background=nord_fox['blue']),
        left_arrow(nord_fox['blue'], nord_fox['orange']),
        Battery(
            background=nord_fox['orange'],
            format='Battery \uf240  {percent:2.0%}'
        ),
        left_arrow(nord_fox['orange'], gruvbox['blue']),
        PulseVolume(background=gruvbox['blue']),
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
