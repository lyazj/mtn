#!/bin/python3

from mtncfg import *

with open(file_list) as lst:
  files = lst.read()
print(files, end = '')
