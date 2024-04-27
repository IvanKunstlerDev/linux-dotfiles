#!/bin/bash

volume="$(pamixer --get-volume)"
mute="$(pamixer --get-mute)"

get_volume_icon() {
    if [[ $volume -le 33 && $volume -gt 0 && "$mute" == "false" ]]; then
        echo ""

    elif [[ $volume -gt 33 && $volume -lt 66 && "$mute" == "false" ]]; then
        echo ""

    elif [[ $volume -gt 66 && "$mute" == "false" ]]; then
        echo ""

    elif [[ $volume -eq 0 || "$mute" == "true" ]]; then
        echo ""

    fi
}

if [[ "$1" == "--volume" ]]; then
    echo $volume

elif [[ "$1" == "--icon" ]]; then
    get_volume_icon

fi