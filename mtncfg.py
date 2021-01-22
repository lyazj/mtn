#!/dev/null

import os, sys, shutil

dir_work = os.path.dirname(__file__)
dir_org = os.path.join(dir_work, 'org')
dir_new = os.path.join(dir_work, 'new')
file_list = os.path.join(dir_work, 'list.txt')

dir_bin = '/usr/local/bin'
bin_head = '#!/bin/bash\n\n'
dict_bins = {
  'mtnrew' : 'rewrite.py',
  'mtnupd' : 'update.py',
  'mtnrec' : 'recovery.py',
  'mtnlst' : 'list.py',
}

for d in dir_org, dir_new:
  if not os.path.exists(d):
    os.mkdir(d)
if not os.path.exists(file_list):
  with open(file_list, 'w'):
    pass

def get_backup_name(name):
  return os.path.join(dir_org, os.path.basename(name))

def get_sync_name(name):
  return os.path.join(dir_new, os.path.basename(name))
