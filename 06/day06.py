#!/usr/bin/env python3

import os
import re
import sys

def processInput (_input):

  _x,_p1,_p2 = 0,0,0
  _t,_d = [],[]
  for _line in _input:
    _x += 1
    _line = _line.strip()

    if not _line:
        print("*******Emtpy Line Found at: ", _x)
        next
    elif _m := re.match('^Time:\s*([\d\s]*)', _line):
      _t = re.findall('\d+', _m.group(1))
      #print(_t)
    elif _m := re.match("^Distance:\s*([\d\s]*)", _line):
      _d = re.findall('\d+', _m.group(1))
      #print(_d)

  _i = 0
  _win = []
  while ( _i < len(_t) ):
    _h = 0
    _win.append(0)
    while ( _h <= int(_t[_i]) ):
      if ( (int(_t[_i]) - _h) * _h > int(_d[_i])):
        _win[_i] += 1
      _h += 1
    _i += 1

  _p1 = 1
  for _w in _win:
    _p1 *= _w

### P2 ###
  _j = 0
  while ( _j <= int(''.join(_t)) ):
      if ( (int(''.join(_t)) - _j) * _j > int(''.join(_d))):
        _p2 += 1
      _j += 1
  
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
