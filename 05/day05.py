#!/usr/bin/env python3

import os
import re
import sys
import pprint

def processInput (_input):

  _x,_p1,_p2 = 0,0,0
  _src, _dst = "",""
  _seeds = []
  _map = {}

  for _line in _input:
    _line = _line.strip()
    _x += 1

    if not _line:
#        print("*******Emtpy Line Found at: ", _x)
        next
    elif (_m := re.match("^seeds:\s+(\d[\d\s]*)$", _line)):
      _seeds = _m.group(1).split(" ")
    elif (_m := re.match("^([^\-\s]+)-to-([^\-\s]+)\smap:$", _line)):
      _src = _m.group(1)
      _dst = _m.group(2)
      _map[_src] = {}
      _map[_dst] = {}
      _map[_src]["next"] = _dst
    elif (_m := re.match("^(\d+)\s*(\d+)\s*(\d+)$", _line)):
      _dstart = int(_m.group(1))
      _sstart = int(_m.group(2))
      _len = int(_m.group(3))
      _tmp = dict(map(lambda i,j : (i,j) , range(_sstart, _sstart + _len), range(_dstart, _dstart + _len)))
      _map[_src].update(_tmp)

  _field = {}
  for _seed in _seeds:
    _i = int(_seed)
    _field[_seed] = {}
    _current = "seed"
    while "next" in _map[_current]:
      if _i not in _map[_current]:
        _map[_current][_i] = _i
      _field[_seed][_map[_current]["next"]] = _map[_current][_i]
      _i = _map[_current][_i]
      _current = _map[_current]["next"]
#      print(_seed,"current: " , _current, " Next", _map[_current]["next"])

  pp = pprint.PrettyPrinter(depth=4)
#  pp.pprint(_map)
  pp.pprint(_field)
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
