#!/usr/bin/env python3

from collections import namedtuple
import itertools as it
LR = namedtuple("LR", "L R")


with open("input") as _inputFile:
    inp = _inputFile.read()

instructions, raw_nodes = inp.split("\n\n")

nodes = {}
for node in raw_nodes.splitlines():
    node, lr = node.split(' = ')
    left, right = lr.strip()[1:-1].split(", ")
    nodes[node] = LR(left, right)


# part 1
node = 'AAA'

steps = 0
for direction_ in it.cycle(instructions.strip()):
    # print(direction_)
    steps += 1
    if direction_ == 'L':
        next_node = nodes[node].L
    else:
        next_node = nodes[node].R
    
    node = next_node
    if node == 'ZZZ':
        print(f"Part 1: {steps}")
        break
        

# part 2

p2 = [node for node in nodes if node.endswith('A')]

def p2_runner(node):
    steps = 0
    for direction_ in it.cycle(instructions.strip()):
        steps += 1
        if direction_ == 'L':
            next_node = nodes[node].L
        else:
            next_node = nodes[node].R
        
        node = next_node
        if node.endswith('Z'):
            return steps

lcms = [p2_runner(node) for node in p2]
from math import lcm
print(f"Part 2: {lcm(*lcms)}")
