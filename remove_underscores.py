#!/usr/bin/python3
import os
import sys

filename = sys.argv[1]

new_filename = filename
new_filename = new_filename.replace('_', ' ')
if new_filename[0:3] == 'EN-':
    new_filename = new_filename[3:]
#print(filename)
#print(new_filename)

os.rename(filename, new_filename)
