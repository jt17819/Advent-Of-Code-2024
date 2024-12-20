import numpy as np
import re, ast

def main():
    with open("Day 03/data.txt", "r") as file:
        data = file.read().split("\n")
    # print(data)

    total = 0
    for line in data:
        mults = re.findall(r"mul(\([0-9]+,[0-9]+\))", line)

        for mult in mults:
            a, b = ast.literal_eval(mult)
            total += a * b

    return total

if __name__ == "__main__":
    print(main())
