import numpy as np
import re


def main():
    with open("Day 13/data.txt", "r") as file:
        data = file.read()
    # data = np.loadtxt("Day 13/data.txt", dtype=str)
    # print(data)
    a_buttons = re.findall(r"A: X(.[0-9]+), Y(.[0-9]+)", data)
    b_buttons = re.findall(r"B: X(.[0-9]+), Y(.[0-9]+)", data)
    prizes = re.findall(r"Prize: X=(.[0-9]+), Y=(.[0-9]+)", data)
    
    machines = zip(a_buttons, b_buttons, prizes)
    total = 0
    for machine in machines:
        a, b, prize = machine
        a = (int(a[0]), int(a[1]))
        b = (int(b[0]), int(b[1]))
        prize = (int(prize[0]), int(prize[1]))

        a_presses = 0
        b_presses = 0
        cost = 10000
        while b_presses * b[0] < prize[0] and b_presses * b[1] < prize[1]:
            b_presses += 1
        while b_presses:
            b_presses -= 1
            while (a_presses * a[0] + b_presses * b[0]) < prize[0] and (a_presses * a[1] + b_presses * b[1]) < prize[1]:
                a_presses += 1
                
            if (a_presses * a[0] + b_presses * b[0]) == prize[0] and (a_presses * a[1] + b_presses * b[1]) == prize[1]:
                cost = min(cost, a_presses * 3 + b_presses)

        if cost < 10000:
            total += cost
    
    return total


if __name__ == "__main__":
    print(main())
