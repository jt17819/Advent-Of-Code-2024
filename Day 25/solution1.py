import numpy as np


def main():
    with open("Day 25/data.txt", "r") as file:
        data = file.read().split("\n\n")
    # data = np.loadtxt("Day 25/data.txt", dtype=str)
    # print(data)
    
    locks, keys = [], []
    for pattern in data:
        rows = pattern.split("\n")
        height = [0] * len(rows[0])
        for row in rows:
            for i in range(len(row)):
                if row[i] == "#":
                    height[i] += 1

        if rows[0][0] == "#":
            locks.append(height)
        else:
            keys.append(height)

    max_height = len(rows)
    count = 0
    for lock in locks:
        for key in keys:
            if not any((lock[i] + key[i]) > max_height for i in range(len(lock))):
                count += 1
    return count


if __name__ == "__main__":
    print(main())
