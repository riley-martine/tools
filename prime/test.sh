#!/bin/bash
while read -r line; do
    prime=$(./prime $line)
    if [ $prime != 1 ]
    then
        echo $line
    fi
done < "10000.txt"

while read -r line; do
    prime=$(./prime $line)
    if [ $prime != 0 ]
    then
        echo $line
    fi
done < "composites.txt"
