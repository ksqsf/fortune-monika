#!/usr/bin/env python3

import re

DIALOG_PATTERN=r'(?<=^    m ").*(?=")'
pat = re.compile(DIALOG_PATTERN)

with open('script-ch30.rpy') as f:
  in_dialog = False
  for line in f:
    if line[0] == '#': continue
    mat = pat.search(line)
    if mat:
      print(mat.group())
      in_dialog = True
    elif in_dialog and line[0] != ' ':
      print('%')
      in_dialog = False
