#!/usr/bin/env python3

import os
import re
import sys

def processInput (_input):

  _x,_p1,_p2 = 0,0,0
  _dirs = ""
  _map = {}
  _a = []
  for _line in _input:
    _x += 1
    _line = _line.strip()

    if not _line:
        print("*******Emtpy Line Found at: ", _x)
        next
    elif _d := re.match("^([RL]*)$",_line):
        _dirs = _d.group(1)
    elif _q := re.match("^(\S*)\s*=\s*\((\S*),\s*(\S*)\)$",_line):
      _map[_q.group(1)] = {"L" : _q.group(2), "R" : _q.group(3)}
      if re.match("^\S\SA\s*", _q.group(1)):
          _a.append(_q.group(1))

#  _s = "AAA"
#  while _s != "ZZZ":
#    for _c in _dirs:
#      _p1 += 1
#      _s = _map[_s][_c]

  _r = re.compile("^\S\SZ")

  _c = 0
  while len(list(filter(_r.match,_a))) != len(_a): 
      for _ai, _step in enumerate(_a):
          _d = _dirs[_c]
          _a[_ai] = _map[_step][_d]
      _c += 1
      if (_c >= len(_dirs)):
        _c = _c - len(_dirs)
      _p2 += 1


  print("Day  Part 1: ", _p1)
  print("Day  Part 2: ", _p2)


def p1():
  print("p1")

def p2():
  print("p2")

def main(_filePath):
    
  if not os.path.isfile(_filePath):
    print(_filePath + " does not appear to be a file")
    exit(1)

  with open(_filePath) as _inputFile:
    _input = _inputFile.readlines()

  processInput(_input)

if __name__ == '__main__':
    
  filePath = "input"

  if len(sys.argv) > 1:
    filePath = sys.argv[1]

  main(filePath)
