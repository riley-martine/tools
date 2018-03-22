#!/bin/bash

# Script to replace ping and see if I'm connected to the internet
# Prints 0 for no and 1 for yes

echo $(expr 1 - $(curl wral.com 2>&1 >/dev/null | grep -c resolve))
