#!/bin/python3

from mtncfg import *

if len(sys.argv) == 1:
  print(__file__ + ': missing file operand')
  sys.exit(1)

target = sys.argv[1]
if os.path.isdir(target):
  print(__file__ + ": cannot recovery '" + target
      + "'. It is a directory")
  sys.exit(1)

backup = get_backup_name(target)
with open(file_list, 'r') as lst:
  files = lst.read()
  for itm in files.split('\n'):
    if os.path.realpath(itm) == os.path.realpath(target):
      files = files.replace(itm + '\n', '')
      break
  else:
    print(__file__ + ": cannot recovery '" + target
        + "'. It has no backup")
    sys.exit(1)

with open(file_list, 'w') as lst:
  lst.write(files)

sync = get_sync_name(target)
if os.path.exists(sync):
  os.remove(sync)

if os.path.exists(target):
  os.remove(target)
shutil.copy2(backup, target)
