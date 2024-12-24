import numpy as np


def main():
    # with open("Day 10/data.txt", "r") as file:
    #     data = file.read().split("\n")
    data = np.loadtxt("Day 10/data.txt", dtype=str)
    data = np.array([[int(n) for n in num] for num in data])
    # print(data)
    heads = zip(*np.where(data == 0))

    total = 0
    for head in heads:
        total += traverse(data, head)

    return total


def traverse(lava_map, pos):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr = lava_map[pos[0]][pos[1]]
    
    if curr == 9:
        return 1
    
    count = 0
    for d in dirs:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if 0 <= new_pos[0] < len(lava_map) and 0 <= new_pos[1] < len(lava_map[0]) and  lava_map[new_pos[0]][new_pos[1]] == curr + 1:
            count += traverse(lava_map, new_pos)
    
    return count


if __name__ == "__main__":
    print(main())
