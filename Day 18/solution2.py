import numpy as np
from collections import deque

def main():
    # with open("Day 18/data.txt", "r") as file:
    #     data = file.read().split("\n")
    data = np.loadtxt("Day 18/data.txt", dtype=int, delimiter=",")
    # print(data)

    length = 71
    height = 71

    grid = np.zeros((height, length))

    num_to_process = 1024
    for i in range(num_to_process):
        pos = (data[i][1], data[i][0])
        grid[pos] = 1

    path = get_path(grid)
    for i in range(num_to_process, len(data)):
        pos = (data[i][1], data[i][0])
        grid[pos] = 1

        if pos in path:
            path = get_path(grid)
            if not path:
                return data[i]
    return None


def get_valid_neighbours(pos, grid, visited):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    height = len(grid)
    length = len(grid[0])
    valid = []
    for d in dirs:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if 0 <= new_pos[0] < height and 0 <= new_pos[1] < length and grid[new_pos] == 0 and new_pos not in visited:
            valid. append(new_pos)

    return valid


def get_path(grid):
    height = len(grid)
    length = len(grid[0])
    start = (0, 0)
    end = (height - 1, length - 1)
    open_nodes = deque([(start, [])])
    visited = set()

    while open_nodes:
        pos, path = open_nodes.popleft()
        if pos == end:
            return path
        
        for new_pos in get_valid_neighbours(pos, grid, visited):
            open_nodes.append((new_pos, path + [new_pos]))
            visited.add(new_pos)

    return None


if __name__ == "__main__":
    print(main())
