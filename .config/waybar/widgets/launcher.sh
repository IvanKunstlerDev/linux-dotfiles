#!/bin/bash

eww_power="eww -c $HOME/.config/eww/power-menu"
power_visible="$($eww_power get power_visible)"

eww_music="eww -c $HOME/.config/eww/media-control"
music_visible="$($eww_music get music_visible)"


music_widget() {
    if [[ $music_visible == false ]]; then
        $eww_music open music-window
        $eww_music update music_visible=true
    
    elif [[ "$music_visible" == "true" ]]; then
        $eww_music close music-window
        $eww_music update music_visible=false

    fi
}


if [[ "$1" == "--music" ]]; then
    music_widget

elif [[ "$1" == "--power" ]]; then
    $eww_power open power-window

fi