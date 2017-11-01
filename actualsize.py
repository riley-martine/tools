#!/usr/bin/env python3.6
"""show info page with actual size of files + folders"""
import sys
import os
import subprocess
import tabulate
from tkinter import *

# http://stackoverflow.com/questions/1392413/calculating-a-directory-size-using-python


def du(path):
    """disk usage in human readable format (e.g. '2,1GB')"""
    return subprocess.check_output(['sudo', 'du', '-sh', path]).split()[0].decode('utf-8')


def du_not_sh(path):
    return subprocess.check_output(['sudo', 'du', '-sb', path]).split()[0].decode('utf-8')

cwd = sys.argv[1]
item_sizes = []
for item in os.listdir(sys.argv[1]):
    item_abs = os.path.join(cwd, item)
    size = du(item_abs)
    size_bytes = int(du_not_sh(item_abs))

    if len(item) > 18:
        item = item[:15] + "..."

    item_sizes.append(
        (item, size, size_bytes)
    )

item_sizes.sort(key=lambda x: x[2], reverse=True)
item_sizes = [i[:2] for i in item_sizes]

master = Tk()
master.title("Size Info")

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(master, yscrollcommand=scrollbar.set, width=30)
text.insert(END, tabulate.tabulate(item_sizes, headers=("Item", "Size")))
text.pack(side=LEFT, fill=BOTH)
text.config(state=DISABLED)

scrollbar.config(command=text.yview)

mainloop()
