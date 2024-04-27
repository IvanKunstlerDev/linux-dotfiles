#!/bin/sh

# Keybord config
setxkbmap es &

# Mouse config
xinput --set-prop 'Logitech USB Optical Mouse' 'libinput Accel Speed' '-0.46'

xinput set-prop "Logitech USB Optical Mouse" "libinput Accel Profile Enabled" 0 1 0

# Restore wallpaper
nitrogen --restore &

# Start picom to transparence and other effects
picom --config ".config/picom/picom.conf" &

# Systray icons
nm-applet &
volumeicon &
