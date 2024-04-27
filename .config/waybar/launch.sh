#!/bin/sh

# Quit all waybar instances
killall waybar

if [[ $USER = "SavannoxDev" ]]
then
	waybar -c ~/.config/waybar/config -s ~/.config/waybar/style.css
else
	waybar &
fi
