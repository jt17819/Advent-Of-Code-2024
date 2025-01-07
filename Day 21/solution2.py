import numpy as np
import re
from functools import lru_cache


def main():
    with open("Day 21/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 21/data.txt", dtype=str)
    # print(data)
    global numpad_graph
    global dirpad_graph
    numpad_graph, dirpad_graph = create_graphs()

    total = 0
    for code in data:
        multiplier = int(re.findall("[0-9]+", code)[0])
        length = get_length(code, 26, True)

        total += length * multiplier
    return total


def create_graphs():
    numpad  = {
        '7': (0, 0), '8': (0, 1), '9': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '1': (2, 0), '2': (2, 1), '3': (2, 2),
                     '0': (3, 1), 'A': (3, 2),
    }
    dirpad = {
                     '^': (0, 1), 'A': (0, 2),
        '<': (1, 0), 'v': (1, 1), '>': (1, 2),
    }
    
    numpad_graph = {}
    for num1, (y1, x1) in numpad.items():
        for num2, (y2, x2) in numpad.items():
            part = '<' * (x1 - x2) +  'v' * (y2 - y1) + '^' * (y1 - y2) + '>' * (x2 - x1)
            
            if (y1, x2) == (3, 0) or (y2, x1) == (3, 0):
                part = part[::-1]
            
            numpad_graph[(num1, num2)] = part + "A"
            
    dirpad_graph = {}
    for num1, (y1, x1) in dirpad.items():
        for num2, (y2, x2) in dirpad.items():
            part = '<' * (x1 - x2) +  'v' * (y2 - y1) + '^' * (y1 - y2) + '>' * (x2 - x1)
            
            if (y1, x2) == (0, 0) or (y2, x1) == (0, 0):
                part = part[::-1]
            
            dirpad_graph[(num1, num2)] = part + "A"
    
    return numpad_graph, dirpad_graph


@lru_cache
def get_length(code, count, first=False):
    if count == 0:
        return len(code)
    
    graph = numpad_graph if first else dirpad_graph
    prev = "A"
    total = 0
    
    for char in code:
        total += get_length(graph[(prev, char)], count - 1)
        prev = char
    
    return total


if __name__ == "__main__":
    print(main())
