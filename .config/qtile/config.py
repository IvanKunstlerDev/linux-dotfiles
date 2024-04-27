import os
import subprocess

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "kitty"

transparent = "#00000000"
tokyo_night = {
    "rose": "#f7768e",
    "orange": "#ff9e64",
    "yellow": "#e0af68",
    "green": "#9ece6a",
    "cyan": "#73daca",
    "light_blue": "#b4f9f8",
    "sky": "#2ac3de",
    "lighter_blue": "#7dcfff",
    "blue": "#7aa2f7",
    "violet": "#bb9af7",
    "gray1": "#c0caf5",
    "gray2": "#a9b1d6",
    "gray3": "#9aa5ce",
    "peach": "#cfc9c2",
    "gray4": "#565f89",
    "gray5": "#414868",
    "gray6": "#24283b",
    "black": "#1a1b26",
}

keys = [
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),

    Key([mod], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "t", lazy.window.toggle_floating()),
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    Key([mod], "Up", lazy.spawn("pamixer -i 2")),
    Key([mod], "Down", lazy.spawn("pamixer -d 2")),
]

groups_icons = {
    1: Group("1", label=""),
    2: Group("2", label=""),
    3: Group("3", label=""),
    4: Group("4", label=""),
    5: Group("5", label=""),
}

groups = [groups_icons[i] for i in groups_icons]

def get_group_key(name):
    return[k for k, g in groups_icons.items() if g.name == name][0]

for i in groups:
    keys.extend(
        [
            Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen()),
            Key(
                [mod, "shift"], str(get_group_key(i.name)), lazy.window.togroup(i.name, switch_group=True)
            ),
        ]
    )

layouts = [
    layout.MonadTall(
        border_normal=tokyo_night["gray5"],
        border_focus=tokyo_night["gray3"],
        margin=8,
        border_width=0,
    ),
    layout.Columns(
        border_normal=tokyo_night["gray5"],
        border_focus=tokyo_night["gray3"],
        margin=8,
        border_width=0,
    ),
    layout.Max(),
]

widget_defaults = dict(
    font="Ubuntu",
    fontsize=16,
    padding=0,
    foreground=tokyo_night["gray1"]
)
extension_defaults = widget_defaults.copy()

def get_icon_widget(icon, size=26, pd=5, fg=tokyo_night["gray1"]):
    return widget.TextBox(
        font="Hack Nerd Font Mono",
        text=icon,
        fontsize=size,
        background=transparent,
        foreground=fg,
        padding=pd,
    )

def separator(size, bg=transparent):
    return widget.Sep(
        foreground=transparent,
        background=bg,
        linewidth=size,
    )

screens = [
    Screen(
        top=bar.Bar(
            [
                separator(12),
                widget.Volume(
                    padding=5,
                    fontsize=21,
                    emoji=True,
                    emoji_list=["󰝟", "󰕿", "󰖀", "󰕾"],
                    max_chars=1
                ),
                widget.Volume(
                    fmt="{}"
                ),
                separator(12),

                get_icon_widget("󰃠"),
                widget.TextBox("100%"),
                
                separator(12),
                widget.WindowName(
                    format="|   {name}"
                ),

                widget.Spacer(),
                widget.GroupBox(
                    highlight_method='block',
                    fontsize=24,
                    block_highlight_text_color=tokyo_night["gray1"],
                    inactive=tokyo_night["gray6"],
                    active=tokyo_night["gray4"],
                    this_current_screen_border=transparent
                ),
                widget.Spacer(),

                separator(12),
                get_icon_widget(""),
                widget.CheckUpdates(
                    custom_command="checkupdates",
                    execute="alacritty -e sudo pacman -Syu",
                    display_format="{updates}",
                    colour_have_updates=tokyo_night["gray1"],
                    update_interval=1700
                ),
                
                separator(12),
                get_icon_widget("󰘚"),
                widget.Memory(
                    format='{MemPercent:.0f}%'
                ),
                
                separator(12),
                get_icon_widget(""),
                widget.Clock(
                    format="%d %b - %A"
                ),

                separator(12),
                get_icon_widget("󰥔"),
                widget.Clock(
                    format="%H:%M"
                ),

                separator(12),
                widget.QuickExit(
                    default_text="󰤆",
                    fontsize=20,
                    padding=5,
                    countdown_start=1
                ),
                separator(12),
            ],
            size=28,
            background=transparent,
            margin = [2, 8, -4, 8]
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([script])
