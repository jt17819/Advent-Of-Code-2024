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
    
    start = (0, 0)
    end = (height - 1, length - 1)
    open_nodes = deque([(start, 0)])
    visited = set()

    while open_nodes:
        pos, dist = open_nodes.popleft()
        if pos == end:
            return dist
        
        for new_pos in get_valid_neighbours(pos, grid, visited):
            open_nodes.append((new_pos, dist + 1))
            visited.add(new_pos)

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


if __name__ == "__main__":
    print(main())
