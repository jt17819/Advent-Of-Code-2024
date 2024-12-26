import numpy as np


def main():
    with open("Day 15/data.txt", "r") as file:
        data = file.read().split("\n\n")
    # data = np.loadtxt("Day 15/data.txt", dtype=str)
    # print(data)
    double_data = data[0]
    double_data = double_data.replace("#", "##")
    double_data = double_data.replace("O", "[]")
    double_data = double_data.replace(".", "..")
    double_data = double_data.replace("@", "@.")

    grid = np.array([[char for char in line] for line in double_data.split("\n")])
    instructions = "".join(data[1].split("\n"))

    pos = list(zip(*np.where(grid == "@")))[0]
    dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    for instruction in instructions:
        grid, pos = move(grid, pos, dirs[instruction])

    boxes = np.where(grid == "[")
    return sum(boxes[0] * 100) + sum(boxes[1])


def move(grid, pos, d):
    if grid[pos[0] + d[0]][pos[1] + d[1]] == "#":
        return grid, pos

    if grid[pos[0] + d[0]][pos[1] + d[1]] == "[":
        if d in [(0, -1), (0, 1)]:
            grid, _ = move(grid, (pos[0] + d[0], pos[1] + d[1]), d)

        else:
            check1 = check_move(grid, (pos[0] + d[0], pos[1] + d[1]), d)
            check2 = check_move(grid, (pos[0] + d[0], pos[1] + 1 + d[1]), d)
            if check1 and check2:
                grid, _ = move(grid, (pos[0] + d[0], pos[1] + d[1]), d)
                grid, _ = move(grid, (pos[0] + d[0], pos[1] + 1 + d[1]), d)

    if grid[pos[0] + d[0]][pos[1] + d[1]] == "]":
        if d in [(0, -1), (0, 1)]:
            grid, _ = move(grid, (pos[0] + d[0], pos[1] + d[1]), d)

        else:
            check1 = check_move(grid, (pos[0] + d[0], pos[1] + d[1]), d)
            check2 = check_move(grid, (pos[0] + d[0], pos[1] - 1 + d[1]), d)
            if check1 and check2:
                grid, _ = move(grid, (pos[0] + d[0], pos[1] + d[1]), d)
                grid, _ = move(grid, (pos[0] + d[0], pos[1] - 1 + d[1]), d)

    if grid[pos[0] + d[0]][pos[1] + d[1]] == ".":
        grid[pos[0]][pos[1]], grid[pos[0] + d[0]][pos[1] + d[1]] = grid[pos[0] + d[0]][pos[1] + d[1]], grid[pos[0]][pos[1]]
        pos = (pos[0] + d[0], pos[1] + d[1])

    return grid, pos


def check_move(grid, pos, d):
    if grid[pos[0] + d[0]][pos[1] + d[1]] == "#":
        return False

    if grid[pos[0] + d[0]][pos[1] + d[1]] == "[":
        check1 = check_move(grid[:], (pos[0] + d[0], pos[1] + d[1]), d)
        check2 = check_move(grid[:], (pos[0] + d[0], pos[1] + 1 + d[1]), d)
        return check1 and check2

    if grid[pos[0] + d[0]][pos[1] + d[1]] == "]":
        check1 = check_move(grid, (pos[0] + d[0], pos[1] + d[1]), d)
        check2 = check_move(grid, (pos[0] + d[0], pos[1] - 1 + d[1]), d)
        return check1 and check2

    if grid[pos[0] + d[0]][pos[1] + d[1]] == ".":
        return True


if __name__ == "__main__":
    print(main())
