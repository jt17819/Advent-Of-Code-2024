import numpy as np
from collections import deque


def main():
    with open("Day 09/data.txt", "r") as file:
        data = file.read()
    # data = np.loadtxt("Day 09/data.txt", dtype=str)
    data = np.array([int(n) for n in data])
    # print(data)
    files = deque()
    empty = []

    for i, n in enumerate(data):
        if i & 1:
            empty.append(n)
        else:
            for _ in range(n):
                files.append(i // 2)

    system = [0] * sum(data)
    pointer = 0
    i = 0
    while files:
        for _ in range(data[i]):
            if files and i & 1:
                system[pointer] = files.pop()
                pointer += 1
            elif files:
                system[pointer] = files.popleft()
                pointer += 1
        i += 1

    return sum([i * n for i, n in enumerate(system)])


if __name__ == "__main__":
    print(main())
