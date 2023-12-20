#!/usr/bin/env python3

import os
import re
import sys

def processInput (_input):

  _p1,_p2 = 0,0;
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
  _first = re.match("^[^\d]*(\d).*$", _line)
  _last = re.match("^.*(\d)[^\d]*$", _line)
  if _first and _last:
    return int(_first.group(1) + _last.group(1))
  else:
    print("***P1*** First: ", _first.groups(), "Last:", _last.groups(), "Line:", _line)

def p2(_line):
  _first = re.search("(\d|one|two|three|four|five|six|seven|eight|nine)", _line)
  _last = re.search("(?s:.*)(\d|one|two|three|four|five|six|seven|eight|nine)", _line)
  if _first and _last:
    return int(string2string(_first.group(1)) + string2string(_last.group(1)))
  else:
    print("******P2****** First: ", _first.groups(), "Last:", _last.groups(), "Line:", _line)

def string2string(_string):
  _map = {
    "1":	"1",
    "2":	"2", 
    "3":	"3", 
    "4":	"4", 
    "5":	"5", 
    "6":	"6", 
    "7":	"7", 
    "8":	"8", 
    "9":	"9", 
    "one":	"1", 
    "two":	"2", 
    "three":	"3", 
    "four":	"4", 
    "five":	"5", 
    "six":	"6", 
    "seven":	"7", 
    "eight":	"8", 
    "nine":	"9"
  }

  return _map[_string]

 

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
