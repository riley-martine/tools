#!/bin/bash
sides[0]='Heads'
sides[1]='Tails'

echo ${sides[$[RANDOM % 2]]}
