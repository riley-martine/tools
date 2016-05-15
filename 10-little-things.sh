#!/bin/bash

diff --suppress-common-lines <(sed 's/ .*//' /home/riley/Documents/filesystem.manifest) <(apt-mark showmanual | sort | uniq) | grep '>' | sed 's/[>] //' > /home/riley/backups/packages.txt

cp /etc/hosts /home/riley/backups
cp /home/riley/.gitconfig /home/riley/backups
cp /home/riley/.zsh* /home/riley/backups
cp /etc/fstab /home/riley/backups

cp -r /home/riley/.oh-my-zsh/ /home/riley/backups
cp -r /home/riley/Documents/ /home/riley/backups
cp -r /usr/share/zsh /home/riley/backups/usr/share
cp -r /home/riley/Tools/ /home/riley/backups

