#!/bin/python3

from mtncfg import *

with open(file_list, 'r') as lst:
  files = lst.read()

for itm in files.split('\n'):
  if os.path.exists(itm):
    try:
      shutil.copy2(itm, get_sync_name(itm))
    except SameFileError:
      print("skipped: '" + itm + "'")
      continue
    print("updated: '" + itm + "'")
