# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List
import os 
import re 
import socket 
import subprocess



mod = "mod4"
terminal = "alacritty" 
browser = "firefox"

keys = [

    #focus on windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "p", lazy.layout.next(), desc="Move window focus to other window"),

    #move windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    #resize windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    
    #windows original size
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    #lauch terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    #toogle layout
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    #kill windows
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),

    #reload config
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),

    #shutdown qtile
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    #app laucher
    Key([mod], "space", lazy.spawn("rofi -show run"), desc="Spawn a command using a prompt widget"),

    #firefox
    Key([mod], "b", lazy.spawn("firefox"), desc="lauch firefox"),



]


#-------------GROUPS-------------------
groups = [Group(i) for i in [
     "DEV", "WEB", "DOC", "VM", "WORK", "CHAT", "MUS", "ANIM" 
]]

for i, group in enumerate(groups):
    actual_key = str(i+1)
    keys.extend([
        #SWitch workspacesc
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        #put something in whatever workspaces
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])


#-----------Layouts-------------------

#layouts themes
layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "#373b41",
                "border_normal": "#1d1f21" 
               }   


layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),    
    layout.Bsp(**layout_theme),
    layout.MonadTall(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


#colors
colors = [["#1d1f21", "#1d1f21"],#0
          ["#282a2e", "#282a2e"],#1
          ["#373b41", "#373b41"],#2
          ["#c5c8c6", "#c5c8c6"],#3
          ["#969896", "#969896"],#4
          ["#cc6666", "#cc6666"],#5
          ["#de935f", "#de935f"],#6
          ["#f0c674", "#f0c674"],#7
          ["#b5bd68", "#b5bd68"],#8
          ["#8abeb7", "#8abeb7"],#9
          ["#81a2be", "#81a2be"],#10
          ["#b294bb", "#b294bb"]]#11

#default widget config
widget_defaults = dict(
    font="Ubuntu Bold",
    foreground = colors[3],
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                
                widget.GroupBox(
                    font = "Ubuntu Bold",
                    fontsize = 11,
                    disable_drag = True,
                    borderwidth = 1,
                    active = colors[3],
                    inactive = colors[4] ,
                    rounded = False,
                    highlight_color = colors[0],
                    highlight_method = "line",
                    this_current_screen_border = colors[4] , 
                    this_screen_border = colors[0],
                    other_current_screen_border = colors[2],
                    other_screen_border = colors[3],
                    block_highlight_text_color = colors[3],
                    foreground = colors[2],
                    background = colors[0],
               ),
                
                widget.TextBox(
                    text='\uE0B0',
                    background=colors[2],
                    foreground=colors[0],
                    padding=0,
                    fontsize=25,
                ),

                widget.WindowName(),

                widget.Spacer(),

                widget.Systray(
                    icon_size = 20,
                    margin_y = 4,
                    padding = 10,
                ),
                widget.TextBox(
                    text='\uE0B2',
                    background=colors[2],
                    foreground=colors[0],
                    padding=0,
                    fontsize=25,
                ),
                widget.CurrentLayout(
                    fontsize = 12,
                    font = "Ubuntu Bold",
                    padding = 4,
                    margin_y = 6,
                    background = colors[0],
                ),

                widget.TextBox(
                    text='\uE0B2',
                    background=colors[0],
                    foreground=colors[2],
                    padding=0,
                    fontsize=25,
                ),

                widget.CheckUpdates(
                    distro = 'Arch',
                    display_format = 'Updates: {updates}',
                    update_interval=1800,
                    no_update_string='No updates',
                    colour_have_updates=colors[3],
                    colour_no_updates=colors[3],
                ),
                widget.TextBox(
                    text='\uE0B2',
                    background=colors[2],
                    foreground=colors[0],
                    padding=0,
                    fontsize=25,
                ),

                widget.DF(
                    visible_on_warn=False,
                    background = colors[0],
                    format = ': {p} {uf}{m}|{s}{m}',
                ),

                widget.TextBox(
                    text='\uE0B2',
                    background=colors[0],
                    foreground=colors[2],
                    padding=0,
                    fontsize=25,
                ),

                widget.CPU(
                    format = ": {freq_current}GHz {load_percent}%",
                ),

                widget.TextBox(
                    text='\uE0B2',
                    background=colors[2],
                    foreground=colors[0],
                    padding=0,
                    fontsize=25,
                ),
                widget.Memory(
                    measure_mem='M',
                    format = ":{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}",
                    background = colors[0],
                ),

                widget.TextBox(
                    text='\uE0B2',
                    background=colors[0],
                    foreground=colors[2],
                    padding=0,
                    fontsize=25,
                ),
                widget.Volume(
                    fmt = ": {}",
                ),
                widget.TextBox(
                    text='\uE0B2',
                    background=colors[2],
                    foreground=colors[0],
                    padding=0,
                    fontsize=25,
                ),
                widget.Clock(
                    format = ": %H:%M",
                    background = colors[0],
                ),
           
            ],
            25,
            background=colors[2],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
           # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            
       
    ),
)
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
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
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.


#autostart apps 
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])




wmname = "LG3D"

