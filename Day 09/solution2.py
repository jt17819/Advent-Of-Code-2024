import numpy as np
from collections import deque


def main():
    with open("Day 09/data.txt", "r") as file:
        data = file.read()
    # data = np.loadtxt("Day 09/data.txt", dtype=str)
    data = np.array([int(n) for n in data])
    # print(data)
    files = deque()
    empty = deque()
    pointer = 0
    for i, n in enumerate(data):
        if i & 1 and n:
            empty.append((pointer, n))
        elif n:
            files.append((i // 2, pointer, n))
        pointer += n

    system = [0] * sum(data)
    i = 0

    while files:
        id, pointer, n = files.pop()
        stack = []
        space = 0
        remaining_space = (0, 0)
        
        if empty:
            idx, space = empty.popleft()

        while empty and space < n:
            stack.append((idx, space))
            idx, space = empty.popleft()

        if space >= n and idx < pointer:
            for _ in range(n):
                system[idx] = id
                idx += 1
            remaining_space = (idx, space - n)
        else:
            for _ in range(n):
                system[pointer] = id
                pointer += 1

        if remaining_space[1]:
            stack.append(remaining_space)
            stack.sort(key=lambda x: x[0])
        while stack:
            empty.appendleft(stack.pop())

    # print(system)
    return sum([i * n for i, n in enumerate(system)])


if __name__ == "__main__":
    print(main())
