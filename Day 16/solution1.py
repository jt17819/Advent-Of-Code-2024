import numpy as np
from collections import deque


def main():
    with open("Day 16/data.txt", "r") as file:
        data = file.read().split("\n")
    data = np.array([[char for char in line] for line in data])
    # print(data)

    start = next(zip(*np.where(data == "S")))
    end = next(zip(*np.where(data == "E")))
    # print(start, end)

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_dir = (0, 1)
    open_nodes = deque([(start, curr_dir, 0)])
    score_array = np.full_like(data, 10000000, dtype=int)

    while open_nodes:
        node, curr_dir, score = open_nodes.popleft()

        if data[node] == "#" or score_array[node] < score:
            continue

        score_array[node] = score
        for d in dirs:
            new_node = (node[0] + d[0], node[1] + d[1])
            if d == curr_dir:
                open_nodes.append((new_node, d, score + 1))
            else:
                open_nodes.append((new_node, d, score + 1001))

    return score_array[end]


if __name__ == "__main__":
    print(main())
