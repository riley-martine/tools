#!/bin/bash


diff --suppress-common-lines <(sed 's/ .*//' /home/riley/Documents/filesystem.manifest) <(apt-mark showmanual | sort | uniq) | grep '>' | sed 's/[>] //'


#diff --suppress-common-lines\
# <(sed 's/ .*//' /home/riley/Documents/filesystem.manifest\
# <(dpkg --get-selections | sed 's/[ \t].*//') | grep '>' | sed 's/[>] //'

