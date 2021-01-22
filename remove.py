#!/bin/python3

from mtncfg import *

for itm in dict_bins:
  bin_out = os.path.join(dir_bin, itm)
  if(os.path.exists(bin_out)):
    print('removing:', bin_out)
    os.remove(bin_out)
  else:
    print('skipping:', bin_out)
