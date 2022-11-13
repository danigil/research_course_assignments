import sys
import math
from collections import deque

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



l, s, n = [int(i) for i in input().split()]

array = [0 for _ in range(s)]
pointer = 0

program = []
action_signs = {
    ord('>'),
    ord('<'),
    ord('+'),
    ord('-'),
    ord('.'),
    ord(','),
    ord('['),
    ord(']')
}
for _ in range(l):
    program += filter(lambda x: ord(x) in action_signs,[*input()])

PC = 0 # program counter

stop = False

found_brackets = []

def find_brackets():
    global stop
    stack = deque()
    p = 0
    while True:
        if p >= len(program):
            break
        if program[p] == '[':
            stack.append(p)
        elif program[p] == ']':
            if len(stack) > 0:
                found_brackets.append((stack.pop(),p))
            else:
                stop = True
                print("SYNTAX ERROR")
                break
        p+=1
    if len(stack) > 0:
        stop = True
        print("SYNTAX ERROR")


find_brackets()

def shift_left():
    global pointer, stop
    if pointer == 0:
        stop = True
        print("POINTER OUT OF BOUNDS")
    else:
        pointer-=1

def shift_right():
    global pointer, stop
    if pointer == s-1:
        stop = True
        print("POINTER OUT OF BOUNDS")
    else:
        pointer+=1

def increment():
    global pointer, stop
    if array[pointer] == 255:
        stop = True
        print("INCORRECT VALUE")
    else:
        array[pointer]+=1

def decrement():
    global pointer, stop
    if array[pointer] == 0:
        stop = True
        print("INCORRECT VALUE")
    else:
        array[pointer]-=1

def output():
    print(chr(array[pointer]), end="")

def inp():
    array[pointer] = int(input())

def left_bracket():
    global PC
    if array[pointer] == 0:
        for (left,right) in found_brackets:
            if left == PC:
                PC = right
        
def right_bracket():
    global PC
    if array[pointer] != 0:
        for (left,right) in found_brackets:
            if right == PC:
                PC = left

actions = {
    ord('>') : shift_right,
    ord('<') : shift_left,
    ord('+') : increment,
    ord('-') : decrement,
    ord('.') : output,
    ord(',') : inp,
    ord('[') : left_bracket,
    ord(']') : right_bracket
}

while not stop and PC < len(program):
    actions[ord(program[PC])]()
    PC+=1

