#!/bin/python3

from mtncfg import *

if len(sys.argv) == 1:
  print(__file__ + ': missing file operand')
  sys.exit(1)

target = sys.argv[1]
if not os.path.exists(target):
  print(__file__ + ": cannot rewrite '" + target
      + "'. No such file or directory")
  sys.exit(1)
if os.path.isdir(target):
  print(__file__ + ": cannot rewrite '" + target
      + "'. It is a directory")
  sys.exit(1)

backup = get_backup_name(target)
if not os.path.exists(backup):
  shutil.copy2(target, backup)

with open(file_list, 'r+') as lst:
  files = lst.read()
  for itm in files.split('\n'):
    if os.path.exists(itm) and os.path.samefile(itm, target):
      break
  else:
    lst.write(os.path.abspath(target) + '\n')

os.system('vim ' + target)
