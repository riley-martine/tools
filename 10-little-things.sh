#!/bin/bash

diff --suppress-common-lines <(sed 's/ .*//' ~/Documents/filesystem.manifest) <(apt-mark showmanual | sort | uniq) | grep '>' | sed 's/[>] //' > ~/backups/packages.txt

cp /etc/hosts ~/backups
cp ~/.gitconfig ~/backups
cp ~/.zsh* ~/backups
cp ~/.bash* ~/backups
cp /etc/fstab ~/backups

cp -r ~/.oh-my-zsh/ ~/backups
cp -r ~/Documents/ ~/backups
cp -r /usr/share/zsh ~/backups/usr/share
cp -r ~/Tools/ ~/backups

