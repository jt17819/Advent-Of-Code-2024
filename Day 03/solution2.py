import numpy as np
import re, ast

def main():
    with open("Day 03/data.txt", "r") as file:
        data = file.read().split("\n")
    # print(data)

    total = 0
    do = True
    for line in data:
        parts = re.split(r"(don't\(\))|(do\(\))", line)
        for part in parts:
            if part == "don't()":
                do = False
            elif part == "do()":
                do = True
            elif do and part:
                mults = re.findall(r"mul(\([0-9]+,[0-9]+\))", part)
                # print(mults)
                for mult in mults:
                    a, b = ast.literal_eval(mult)
                    total += a * b

    return total

if __name__ == "__main__":
    print(main())
