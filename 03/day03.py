#!/usr/bin/env python3

import os
import re
import sys

def processInput (_input):

  _p1,_p2 = 0,0
  _i = 0
  for _line in _input:
    _line = _line.strip()

    if not _line:
        print("*******Emtpy Line Found at: ", _x)
        next

    for _m in re.finditer("(\d+)", _line):
      _start = max(0,_m.start() - 1)
      _end = min(len(_line), _m.end() + 1)
      _surround = "".join([_input[max(_i - 1 ,0)][_start:_end], _line[_start:_end], _input[min(_i + 1, len(_input) - 1)][_start:_end]])
      if _special := re.match(".*([^A-Za-z0-9\.]).*",_surround):
        _p1 += int(_m.group(1))

    for _a in re.finditer("\*", _line):
      _astart = max(0,_a.start() - 1)
      _aend = min(len(_line), _a.end() + 1)
      _grid = [] 
      _grid.extend(range(_astart,_aend))
      _grid.extend(range(_astart + len(_line), _aend + len(_line)))
      _grid.extend(range(_astart + (len(_line) * 2), _aend + (len(_line) * 2)))
      _gears = []

      _s = ""
      for _l in range(_i-1,_i+2):
        _g = _input[_l]
        _s += _g.strip()

      for _d in re.finditer("\d+", _s):
        if any(_item in _grid for _item in range(_d.start(),_d.end())):
          _gears.append(_d.group())
    
      if len(_gears) == 2:
        _p2 += (int(_gears[0]) * int(_gears[1]))


    _i+=1

      


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
