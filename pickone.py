#!/usr/bin/env python3.6
import sys
import random

if len(sys.argv) < 2:
    print("Usage: pickone <arg1> <arg2>...")
    sys.exit(1)

print(random.choice(sys.argv[1:]))

