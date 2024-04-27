#!/bin/bash

eww_volume="eww -c $HOME/.config/eww/volume-popup"
eww_visible="$($eww_volume get volume_visible)"

$eww_volume update using_volume=true
echo "usando true"

if [[ $eww_visible == false ]]; then
    $eww_volume update volume_visible=true
    $eww_volume open volume-window

fi

check_use() {
    $eww_volume get using_volume
}

change_volume() {
    action=$1
    value=$2

    #pamixer $action $value
}


if [[ "$1" == "--increase" ]]; then
    change_volume -i 5

elif [[ "$1" == "--decrease" ]]; then
    change_volume -d 5

elif [[ "$1" == "--toggle" ]]; then
    change_volume -t

elif [[ "$1" == "--check-use" ]]; then
    check_use

fi


sleep 3
$eww_volume update using_volume=false
echo "usando false"

using="$($eww_volume get using_volume)"

if [[ $using == false ]]; then
    echo "sin uso"
    $eww_volume close volume-window
    $eww_volume update using_volume=false
    echo "definitivamente false"
    $eww_volume update volume_visible=false
    echo "terminado"

elif [[ $using == true ]]; then
    echo "en uso"

fi
