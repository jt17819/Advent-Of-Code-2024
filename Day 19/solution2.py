import numpy as np
from functools import lru_cache


def main():
    with open("Day 19/data.txt", "r") as file:
        data = file.read().split("\n\n")
    # data = np.loadtxt("Day 19/data.txt", dtype=str)
    # print(data)

    towels, designs = data
    towels = tuple(towels.split(", "))
    designs = designs.split("\n")

    total = 0
    for design in designs:
        total += find_pattern(design, towels)

    return total


@lru_cache
def find_pattern(pattern, parts):
    if pattern == "":
        return 1
    
    count = 0
    for part in parts:
        if part == pattern[:len(part)]:
            count += find_pattern(pattern[len(part):], parts)

    return count


if __name__ == "__main__":
    print(main())
