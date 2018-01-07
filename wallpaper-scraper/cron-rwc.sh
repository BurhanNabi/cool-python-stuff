#!/usr/bin/env sh

#/usr/bin/xuserrun 
export DISPLAY=:1
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus

cd ~/bin/
ls >> ~/hello.txt
python change-wall
