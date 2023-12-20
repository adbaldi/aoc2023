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
