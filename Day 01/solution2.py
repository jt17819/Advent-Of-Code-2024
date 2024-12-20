import numpy as np


def main():
    data = np.loadtxt("Day 01/data.txt", dtype=int)
    # print(data)

    a, b = zip(*data)
    counter_b = {}

    for n in b:
        counter_b[n] = counter_b.get(n, 0) + 1

    similarity = 0
    for n in a:
        similarity += counter_b.get(n, 0) * n

    return similarity


if __name__ == "__main__":
    print(main())
