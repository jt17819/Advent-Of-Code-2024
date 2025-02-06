import numpy as np
from collections import deque
import re


def main():
    with open("Day 24/data.txt", "r") as file:
        data = file.read()
    # data = np.loadtxt("Day 24/data.txt", dtype=str)
    # print(data)
    x_init_vals = re.findall("(x[0-9]{2}): ([01])", data)
    y_init_vals = re.findall("(y[0-9]{2}): ([01])", data)
    instructions = re.findall("(.{3}) (AND|OR|XOR) (.{3}) -> (.{3})", data)
    z_regs = re.findall("(z[0-9]{2})", data)

    wire_map = {}
    for in1, op, in2, out in instructions:
        wire_map[out] = (op, in1, in2)

    def make_wire(char, i):
        return f"{char}{i:02}"

    def make_x(i): return make_wire("x", i)
    def make_y(i): return make_wire("y", i)
    def make_z(i): return make_wire("z", i)

    null_vals = {}
    for i in range(len(x_init_vals)):
        null_vals[make_x(i)] = 0
        null_vals[make_y(i)] = 0

    def init_values(i, x, y, carry):
        x_vals = {
            make_x(i): x,
            make_x(i - 1): carry
        }

        y_vals = {
            make_y(i): y,
            make_y(i - 1): carry
        }

        return {**null_vals, ** x_vals, **y_vals}

    # x_bin_val = "".join(v[1] for v in sorted(x_init_vals, reverse=True))
    # y_bin_val = "".join(v[1] for v in sorted(y_init_vals, reverse=True))

    # target_sum = int(x_bin_val, 2) + int(y_bin_val, 2)
    # print(target_sum)
    # print(bin(target_sum))

    operations = {"AND": lambda a, b: a and b,
                  "OR": lambda a, b: a or b, "XOR": lambda a, b: a ^ b}

    def get_val(wire, vals):
        if wire in vals:
            return vals[wire]

        op, in1, in2 = wire_map[wire]
        vals[wire] = operations[op](get_val(in1, vals), get_val(in2, vals))

        return vals[wire]

    def find_wire(op1, ins1):
        for out, (op2, *ins2) in wire_map.items():
            if op1 == op2 and ins1.issubset(set(ins2)):
                return out
        return

    def fix_bit(i):
        curr_x, curr_y = make_x(i), make_y(i)
        prev_x, prev_y = make_x(i-1), make_y(i-1)
        curr_xor = find_wire('XOR', {curr_x, curr_y})
        prev_xor = find_wire('XOR', {prev_x, prev_y})
        direct_carry = find_wire('AND', {prev_x, prev_y})
        recarry = find_wire('AND', {prev_xor})
        carry = find_wire('OR', {direct_carry, recarry})
        z = find_wire('XOR', {curr_xor, carry})
        
        if z is None:
            z_ins = set(wire_map[make_z(i)][1:])
            w1, w2 = z_ins ^ {curr_xor, carry}
        else:
            w1, w2 = {z, make_z(i)}
        wire_map[w1], wire_map[w2] = wire_map[w2], wire_map[w1]
        return {w1, w2}

    swapped_wires = set()

    for i in range(1, 45):
        for x in range(2):
            for y in range(2):
                for c in range(2):
                    if x ^ y ^ c != get_val(make_z(i), init_values(i, x, y, c)):
                        swapped_wires |= fix_bit(i)

    return ','.join(sorted(swapped_wires))


if __name__ == "__main__":
    print(main())
