import numpy as np


def main():
    # with open("Day 12/data.txt", "r") as file:
    #     data = file.read().split("\n")
    data = np.loadtxt("Day 12/data.txt", dtype=str)
    data = np.array([[l for l in line] for line in data])
    # print(data)
    letters = np.unique(data)

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    total = 0
    for letter in letters:
        locations = set(zip(*np.where(data == letter)))

        while locations:
            region = []
            open_pos = [next(iter(locations))]
            perimeter = 0

            while open_pos:
                pos = open_pos.pop()
                locations.remove(pos)
                region.append(pos)
                perimeter += 4

                for d in dirs:
                    new_pos = (pos[0] + d[0], pos[1] + d[1])
                    if new_pos in locations:
                        if new_pos not in open_pos:
                            open_pos.append(new_pos)
                        perimeter -= 2

            total += len(region) * perimeter

    return total


if __name__ == "__main__":
    print(main())
