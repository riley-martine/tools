#!/bin/bash


wmctrl -s 1

cd ~/Projects/javaclass/$1

xfce4-terminal
wmctrl -r :ACTIVE: -b add,maximized_vert
wmctrl -r :ACTIVE: -e 0,961,0,951,1010

xfce4-terminal
wmctrl -r :ACTIVE: -e 0,1,0,951,482

xfce4-terminal
wmctrl -r :ACTIVE: -e 0,1,522,951,498

