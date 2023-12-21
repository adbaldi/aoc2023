#!/usr/bin/env python3

import os
import re
import sys
import collections

def processInput (_input):

  _x,_p1,_p2 = 0,0,0
  _orderedHands = []
  _bets = {}

  _hands = { 'five' : {},
             'four' : {},
             'full' : {},
             'three': {},
             'two'  : {},
             'one'  : {},
             'hc'   : {},
             'NA'   : {}
  }
  for _line in _input:
    _x += 1
    _line = _line.strip()
    _line = _line.replace("A","Z")
    _line = _line.replace("K","Y")
    _line = _line.replace("Q","X")
    _line = _line.replace("J","W")

    if not _line:
        print("*******Emtpy Line Found at: ", _x)
        next
    elif ( _hand := re.match("^([\d\w]+)\s*(\d+)$", _line) ):
      print(_hand.groups())
    else:
      print("we got a problem here: ", _x)
    
    _type = "NA"
    _r = collections.Counter(_hand.group(1))
    if ( len(_r) == 5 ):
      _type = "hc"
    elif ( len(_r) == 4 ):
      _type = "one"
    elif ( len(_r) == 3):
      _type = "two"
      for _c in _r:
        if ( _r[_c] == 3):
          _type = "three"
    elif ( len(_r) == 2):
      _type = "full"
      for _c in _r:
        if ( _r[_c] == 4):
          _type = "four"
    elif ( len(_r) == 1 ):
      _type = "five"
    _hands[_type][_hand.group(1)] = _hand.group(2)
    _bets[_hand.group(1)] = _hand.group(2)

  for _t in ["hc", "one", "two", "three", "full", "four", "five"]:
    _orderedHands.extend(sorted(_hands[_t].keys()))

  _i = 1;
  for _h in _orderedHands:
    _p1 += (_i * int(_bets[_h]))
    _i += 1

  print(_hands)
  print(_orderedHands)

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
