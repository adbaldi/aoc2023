#!/usr/bin/env python3

import os
import re
import sys
import math

def processInput (_input):

  _p1,_p2 = 0,0
  for _line in _input:
    _line = _line.strip()

    if not _line:
        print("*******Emtpy Line Found at: ", _x)
        next

    
    _p1 += p1(_line)
    _p2 += p2(_line)

  print("Day  Part 1: ", _p1)
  print("Day  Part 2: ", _p2)


def p1(_line):
  _cubes = {
    "red"	: 12,
    "green"	: 13,
    "blue"	: 14
  }

  _game = re.match("^Game (\d*): (.*)$", _line) 
  print("GAME: ", _game.group(1))

  for _set in _game.group(2).split(";"):
    for _subset in _set.split(","):
      _subset = _subset.strip()
      _cube = re.match("^(\d*)\s*(\w*)$", _subset)
      if int(_cube.group(1)) > _cubes[_cube.group(2)]:
        return 0
  
  return int(_game.group(1))

def p2(_line):
  _cubes = {
    "red"	: 0,
    "green"	: 0,
    "blue"	: 0
  }

  _game = re.match("^Game (\d*): (.*)$", _line) 
  print("GAME: ", _game.group(1))

  for _set in _game.group(2).split(";"):
    for _subset in _set.split(","):
      _subset = _subset.strip()
      _cube = re.match("^(\d*)\s*(\w*)$", _subset)
      if int(_cube.group(1)) > _cubes[_cube.group(2)]:
        _cubes[_cube.group(2)] = int(_cube.group(1))
    
  return math.prod(_cubes.values())

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
