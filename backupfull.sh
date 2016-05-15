#!/bin/bash

rsync -aAX --info=progress2 --delete --exclude={"/etc/fstab","/home/*/.cache/chromium/*","/home/*/.local/share/Trash/*","/home/*/.gvfs","/home/riley/.steam/Steam/steamapps/*","/home/riley/Desktop/Ex\ Machina/*","/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"} / /media/riley/INFECTED
