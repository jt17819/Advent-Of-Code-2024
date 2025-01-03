import numpy as np
import re


def main():
    with open("Day 17/data.txt", "r") as file:
        data = file.read()
    # data = np.loadtxt("Day 17/data.txt", dtype=str)
    # print(data)
    reg_A = int(re.findall("Register A: ([0-9]+)", data)[0])
    reg_B = int(re.findall("Register B: ([0-9]+)", data)[0])
    reg_C = int(re.findall("Register C: ([0-9]+)", data)[0])
    prog = re.findall("Program: ([0-9,]+)", data)[0].split(",")
    
    reg_A = 0
    for i in reversed(range(len(prog))):
        reg_A <<= 3
        while run(prog, reg_A, reg_B, reg_C) != prog[i:]:
            reg_A += 1

    return reg_A


def run(prog, reg_A, reg_B, reg_C):
    opcodes = {"0": "adv", "1": "bxl", "2": "bst", "3": "jnz", "4": "bxc", "5": "out", "6": "bdv", "7": "cdv"}

    pointer = 0
    output = []
    while pointer < len(prog) - 1:
        opcode, operand = opcodes[prog[pointer]], int(prog[pointer + 1])

        match operand:
            case 4:
                combo_operand = reg_A
            case 5:
                combo_operand = reg_B
            case 6:
                combo_operand = reg_C
            case _:
                combo_operand = operand

        match opcode:
            case "adv":
                reg_A //= (2 ** combo_operand)
            case "bxl":
                reg_B ^= operand
            case "bst":
                reg_B = combo_operand % 8
            case "jnz":
                if reg_A != 0:
                    pointer = operand - 2
            case "bxc":
                reg_B ^= reg_C
            case "out":
                output.append(combo_operand % 8)
            case "bdv":
                reg_B = reg_A // (2 ** combo_operand)
            case "cdv":
                reg_C = reg_A // (2 ** combo_operand)

        pointer += 2

    return [str(out) for out in output]


if __name__ == "__main__":
    print(main())
