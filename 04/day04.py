#!/usr/bin/env python3

import os
import re
import sys

def processInput (_input):

  _p1,_p2 = 0,0
  _copies = dict.fromkeys(range(1,len(_input) +1 ), 1)

  for _line in _input:
    _line = _line.strip()

    if not _line:
        print("*******Emtpy Line Found at: ", _x)
        next

    if _games := re.match("^Card\s*(\d*):\s*([\d\s]*)\s*\|\s*([\d\s]*)$",_line):
      _win = re.findall("\d+", _games.group(2))
      _num = re.findall("\d+", _games.group(3))
      _matched = set(_win) & set(_num)
      if len(_matched):
        _p1 += (1 * pow(2, len(_matched) - 1))

        ##### P2 #####
        for _i in range(1,len(_matched) + 1):
           _copies[int(_games.group(1)) + _i] += _copies[int(_games.group(1))]

    else:
      print("no match")

  _p2 = sum(_copies.values())

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
