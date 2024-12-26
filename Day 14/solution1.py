import numpy as np
import re


def main():
    with open("Day 14/data.txt", "r") as file:
        data = file.read()
    # data = np.loadtxt("Day 14/data.txt", dtype=str)
    # print(data)
    pv = re.findall("p=([0-9-]+),([0-9-]+) v=([0-9-]+),([0-9-]+)", data)

    length = 101
    height = 103
    grid = np.array([[0 for _ in range(length)] for _ in range(height)])

    total = 0
    t = 100
    for px, py, vx, vy in pv:
        x = (int(px) + int(vx) * t) % length
        y = (int(py) + int(vy) * t) % height
        grid[y][x] += 1
    

    total = np.sum(grid[0:height//2, 0:length//2]) \
        * np.sum(grid[height//2 + 1:height, 0:length//2]) \
        * np.sum(grid[0:height//2, length//2 + 1:length]) \
        * np.sum(grid[height//2 + 1:height, length//2 + 1:length])

    return total


if __name__ == "__main__":
    print(main())
