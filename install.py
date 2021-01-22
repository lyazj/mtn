#!/bin/python3

from mtncfg import *

for itm in dict_bins:
  bin_out = os.path.join(dir_bin, itm)
  print('writing:', bin_out)
  with open(bin_out, 'w') as out:
    out.write(bin_head)
    out.write(os.path.abspath(
      os.path.join(dir_work, dict_bins[itm])
    ))
    out.write(' $*\n')
  os.system('chmod 755 ' + bin_out)
