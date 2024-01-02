#!/usr/bin/env python3

import os
import re
import sys

def processInput (_input):

  _x,_p1,_p2 = 0,0,0
  for _line in _input:
    _x += 1
    _line = _line.strip()

    if not _line:
        print("*******Emtpy Line Found at: ", _x)
        next

    _p1 += p1(_line)

  print("Day  Part 1: ", _p1)
  print("Day  Part 2: ", _p2)


def p1(_num):
  _nest = 0
  _levels = []
  _levels.append([int(_x) for _x in _num.split(' ')])
  while sum(_levels[_nest]) > 0:
    _idx = 1
    _tmp = []
    while _idx < len(_levels[_nest]):
      _tmp.append(_levels[_nest][_idx] - _levels[_nest][_idx-1])
      _idx += 1
    _levels.append(_tmp)
    _nest += 1

  print(_levels)
  return 0

  

  

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
