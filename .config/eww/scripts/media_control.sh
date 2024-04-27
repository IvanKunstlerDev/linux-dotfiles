#!/bin/bash

get_image() {
    playerctl metadata --follow --format '{{mpris:artUrl}}' |
    while read -r image_url
    do
        formated_url="${image_url/file:\/\//}"
        echo $formated_url
    done
}

if [[ "$1" == "--image" ]]; then
    get_image

fi