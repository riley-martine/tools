#!/usr/bin/env python3.6
import sys
from collections import namedtuple
from datetime import datetime

TimeStruct = namedtuple("Time", ["hours", "minutes"])

def parse_time(base_str):
    
    if base_str == "now":
        base_str = datetime.now().strftime("%I:%M")

    if base_str.endswith(':'):
        base_str = base_str[:-1]
    if ':' in base_str:
        base_hr, base_min = [int(i) for i in base_str.split(':')]
    else:
        base_hr, base_min = [int(base_str), 0]

    base = TimeStruct(hours=base_hr, minutes=base_min)
    
    return base

def time_until(time, now=parse_time("now")):
    new_min = (time.minutes - now.minutes) % 60
    carry_hr = (time.minutes - now.minutes)//60
    sum_hr = (time.hours - now.hours + carry_hr)
    new_hr = sum_hr//13 + sum_hr%13
    return TimeStruct(hours=new_hr, minutes=new_min)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: timeuntil <time>")
        sys.exit(1)
    
    delta = time_until(parse_time(sys.argv[1]))
    
    tmp = ''
    if len(str(delta.minutes)) == 1:
        tmp = '0'
    print(f"{delta.hours}:{tmp}{delta.minutes}")
