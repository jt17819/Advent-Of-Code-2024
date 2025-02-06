import numpy as np
from collections import deque
import re


def main():
    with open("Day 24/data.txt", "r") as file:
        data = file.read()
    # data = np.loadtxt("Day 24/data.txt", dtype=str)
    # print(data)
    init_vals = re.findall("(.{3}): ([01])", data)
    instructions = re.findall("(.{3}) (AND|OR|XOR) (.{3}) -> (.{3})", data)
    z_regs = re.findall("(z[0-9]{2})", data)

    reg = {}
    for k, v in init_vals:
        reg[k] = int(v)

    queue = deque(instructions)
    operations = {"AND": lambda a, b: a and b, "OR": lambda a, b: a or b, "XOR": lambda a, b: a ^ b}
    while queue:
        val1, op, val2, dest = queue.popleft()
        if val1 in reg and val2 in reg:
            reg[dest] = operations[op](reg[val1], reg[val2])
        else:
            queue.append((val1, op, val2, dest))
    bin_z_regs = "".join(str(reg[r]) for r in sorted(z_regs, reverse=True))
    
    return int(bin_z_regs, 2)


if __name__ == "__main__":
    print(main())
