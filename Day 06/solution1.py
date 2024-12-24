import numpy as np


def main():
    with open("Day 06/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 06/data.txt", dtype=str)
    data = np.array([[char for char in line] for line in data])
    # print(data)
    start = np.where(data == "^")
    dirs = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}

    d = (-1, 0)
    count = 1
    row = start[0][0] + d[0]
    col = start[1][0] + d[1]
    while 0 <= row < len(data) and 0 <= col < len(data[0]):
        if data[row][col] == "#":
            row -= d[0]
            col -= d[1]
            d = dirs[d]
        if data[row][col] == ".":
            count += 1
            data[row][col] = "X"
        row += d[0]
        col += d[1]
    
    # print(data)
    return count


if __name__ == "__main__":
    print(main())
