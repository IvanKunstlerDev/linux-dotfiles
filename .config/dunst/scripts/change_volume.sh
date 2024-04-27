#!/bin/bash

notify_tag="volume"

action="$1"
value="$2"

pamixer $action $value


volume="$(pamixer --get-volume)"
mute="$(pamixer --get-mute)"


if [[ $volume == 0 || $mute == true ]]; then
    # Show the sound muted notification
    dunstify -a "volume" -u low -i audio-volume-muted -h string:x-dunst-stack-tag:$notify_tag "Silenciado" 
else
    # Show the volume notification
    dunstify -a "volume" -u low -i audio-volume-high -h string:x-dunst-stack-tag:$notify_tag \
    -h int:value:"$volume" "Volumen ${volume}%"
fi


canberra-gtk-play -i audio-volume-change -d "volume"