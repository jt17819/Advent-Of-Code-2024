import numpy as np


def main():
    with open("Day 06/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 06/data.txt", dtype=str)
    data = np.array([[char for char in line] for line in data])
    # print(data)
    start = np.where(data == "^")
    dirs = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}

    count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            row = start[0][0]
            col = start[1][0]
            d = (-1, 0)
            if i == row and j == start:
                continue
            visited = set()
            temp = data[i][j]
            data[i][j] = "#"
            while 0 <= row < len(data) and 0 <= col < len(data[0]):
                if ((row, col), d) in visited:
                    # print((row, col))
                    count += 1
                    break
                if data[row][col] == "#":
                    row -= d[0]
                    col -= d[1]
                    d = dirs[d]
                # if data[row][col] == ".":
                else:
                    visited.add(((row, col), d))
                    data[row][col] = "X"
                row += d[0]
                col += d[1]
            data[i][j] = temp
    
    # print(data)
    return count


if __name__ == "__main__":
    print(main())
