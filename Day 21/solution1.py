import numpy as np
import re


def main():
    with open("Day 21/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 21/data.txt", dtype=str)
    # print(data)

    total = 0
    for code in data:
        multiplier = int(re.findall("[0-9]+", code)[0])
        code = numeric_robot(code)
        code = directional_robot(code)
        code = directional_robot(code)

        total += len(code) * multiplier
    return total


def numeric_robot(code):
    keypad = np.array([[7,8,9],[4,5,6],[1,2,3],["X",0,"A"]])
    pos = (3, 2)
    instruction = ""
    for key in code:
        row, col = list(zip(*np.where(keypad == key)))[0]
        
        part = '<' * (pos[1] - col) +  'v' * (row - pos[0]) + '^' * (pos[0] - row) + '>' * (col - pos[1])
        
        if (pos[0], col) == (3, 0) or (row, pos[1]) == (3, 0):
            part = part[::-1]
        instruction += part + "A"
        pos = (row, col)

    return instruction


def directional_robot(code):
    keypad = np.array([["X","^","A"],["<","v",">"]])
    pos = (0, 2)
    instruction = ""

    for key in code:
        row, col = list(zip(*np.where(keypad == key)))[0]
        part = ""
        if row < pos[0]:
            part += "^" * (pos[0] - row)
        else:
            part += "v" * (row - pos[0])
        
        if col < pos[1]:
            part += "<" * (pos[1] - col)
        else:
            part += ">" * (col - pos[1])
            
        if (pos[0], col) == (0, 0) or (row, pos[1]) == (0, 0):
            part = part[::-1]
        instruction += part + "A"
        pos = (row, col)
    
    return instruction


if __name__ == "__main__":
    print(main())
