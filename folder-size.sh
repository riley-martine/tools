#!/bin/bash

DIRS=()
USAGES=()

for line in $@
do
	DIR_USAGE=$(du -s -h $line | cut -f 1)
	$DIRS+="$line"
	$USAGES+="$DIR_USAGE"
done

OUTPUT = ""

$OUTPUT += "Selected directories:\n"

$OUTPUT += $(printf "%10s %10s" $DIRS[0] $USAGES[0])

zenity --info --title "Directory Info" --text "Test $OUTPUT"

#"Selected directories: $DIRS\nDirectory size: $USAGES"