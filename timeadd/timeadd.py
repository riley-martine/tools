#!/usr/bin/env python3.6
import sys
from collections import namedtuple
from datetime import datetime

TimeStruct = namedtuple("Time", ["hours", "minutes"])

def parse_times(base_str, plus_str):
    
    if base_str == "now":
        base_str = datetime.now().strftime("%I:%M")

    if base_str.endswith(':'):
        base_str = base_str[:-1]
    if ':' in base_str:
        base_hr, base_min = [int(i) for i in base_str.split(':')]
    else:
        base_hr, base_min = [int(base_str), 0]

    if plus_str.endswith(':'):
        plus_hr, plus_min = [int(plus_str[:-1]), 0]
    elif plus_str.startswith(':'):
        plus_hr, plus_min = [0, int(plus_str[1:])]
    elif ':' in plus_str:
       plus_hr, plus_min = [int(i) for i in plus_str.split(':')]
    else:
       plus_hr, plus_min = [0, int(plus_str)]
    
    base = TimeStruct(hours=base_hr, minutes=base_min)
    plus = TimeStruct(hours=plus_hr, minutes=plus_min)
    
    return (base, plus)

def add_times(base, plus):
    new_min = (base.minutes + plus.minutes) % 60
    carry_hr = (base.minutes + plus.minutes)//60
    sum_hr = (base.hours + plus.hours + carry_hr)
    new_hr = sum_hr//13 + sum_hr % 13
    return TimeStruct(hours=new_hr, minutes=new_min)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: timeadd <base> <delta>")
        sys.exit(1)
    
    base = sys.argv[1]
    plus = sys.argv[2]
    new_time = add_times(*parse_times(base, plus))
    
    tmp = ''
    if len(str(new_time.minutes)) == 1:
        tmp = '0'
    print(f"{new_time.hours}:{tmp}{new_time.minutes}")
