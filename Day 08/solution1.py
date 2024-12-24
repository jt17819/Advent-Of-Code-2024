import numpy as np


def main():
    # with open("Day 08/data.txt", "r") as file:
    #     data = file.read().split("\n")
    data = np.loadtxt("Day 08/data.txt", dtype=str)
    data = np.array([[l for l in line] for line in data])
    # print(data)

    chars = set(np.unique(data))
    chars.remove(".")
    antinodes = set()
    max_y, max_x = len(data), len(data[0])
    for char in chars:
        pos = list(zip(*np.where(data == char)))
        for i in range(len(pos) - 1):
            for j in range(i + 1, len(pos)):
                dy = pos[i][0] - pos[j][0]
                dx = pos[i][1] - pos[j][1]
                antinode1 = (pos[i][0] + dy, pos[i][1] + dx)
                if 0 <= antinode1[0] < max_y and 0 <= antinode1[1] < max_x:
                    antinodes.add(antinode1)

                antinode2 = (pos[j][0] - dy, pos[j][1] - dx)
                if 0 <= antinode2[0] < max_y and 0 <= antinode2[1] < max_x:
                    antinodes.add(antinode2)
    # print(antinodes)
    # for y, x in antinodes:
    #     data[y][x] = "#"
    # print(data)
    return len(antinodes)


if __name__ == "__main__":
    print(main())
