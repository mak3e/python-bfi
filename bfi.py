#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

def main(code, inp=""):
    mem = [0] * 256                             # Memory of 256 cells
    memp = 0                                    # Memory pointer
    codep = 0                                   # Code pointer
    out = ""                                    # Output string                                    
    while codep<len(code):
        inst = code[codep]                      # Read new instruction
        if inst == "+":                         # If it is + add 1 to value in memory
            mem[memp] = add(mem[memp])
        if inst == "-":                         # If it is - sub 1 from value in memory
            mem[memp] = sub(mem[memp])
        if inst == ">":                         # If it is > move pointer forward
            memp = add(memp)              
        if inst == "<":                         # If it is < move pointer backwards
            memp = sub(memp)
        if inst == ",":                         # If it is , read first character from input
            mem[memp] = ord(inp[0])
            inp=inp[1:]
        if inst == ".":                         # If it is . write character to output
            out += str(chr(mem[memp]))
        if (inst == "[") & (mem[memp] == 0):    # If it is [ and current value is 0, move code pointer to next instruction after the loop
            ncodep = end(code, codep)
        elif inst =="]":                        # If it is ] move code pointer to the start instruction of the loop
            ncodep = start(code, codep) + 1
        else:
            ncodep = codep + 1                  # If it is not [ nor ] move pointer to next instruction
        print("Debug: " + str(mem))             # Print memory
        print("Cmd: " + code[codep])            # Print current instruction
        print("Out: "+out)
        codep=ncodep

def start(code, codep):
    while code[codep] != "[":
        codep -= 1
        if code[codep] == "]":
            codep=start(code, codep)
    return codep - 1

def end(code, codep):
    while code[codep] != "]":
        codep += 1
        if code[codep] == "[":
            codep = end(code, codep)
    return codep + 1


def add(value):
    if value < 255:
        return value + 1
    else:
        return 0

def sub(value):
    if value > 0:
        return value - 1
    else:
        return 255

if __name__ == '__main__':
    if len(sys.argv)>1:
        if len(sys.argv)>2:
            main(sys.argv[1], sys.argv[2])
        else:
            main(sys.argv[1])
