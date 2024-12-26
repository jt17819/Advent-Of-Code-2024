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
    tolerance = 0.0001
    for machine in machines:
        a, b, prize = machine
        a = (int(a[0]), int(a[1]))
        b = (int(b[0]), int(b[1]))
        prize = (int(prize[0]) + 10000000000000, int(prize[1]) + 10000000000000)

        A = (b[0] * prize[1] - b[1] * prize[0]) / ( b[0] * a[1] - b[1] * a[0])
        B = (prize[0] -a[0] * A) / b[0]
        
        if abs(A - round(A)) < tolerance and abs(B - round(B)) < tolerance:
            total += 3*A + B
        
    return int(total)


if __name__ == "__main__":
    print(main())
