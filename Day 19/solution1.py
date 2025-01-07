import numpy as np


def main():
    with open("Day 19/data.txt", "r") as file:
        data = file.read().split("\n\n")
    # data = np.loadtxt("Day 19/data.txt", dtype=str)
    # print(data)

    towels, designs = data
    towels = towels.split(", ")
    designs = designs.split("\n")

    total = 0
    for design in designs:
        total += find_pattern(design, towels)

    return total


def find_pattern(pattern, parts):
    if pattern == "":
        return True
    
    complete = False
    for part in parts:
        if part == pattern[:len(part)]:
            complete = complete or find_pattern(pattern[len(part):], parts)

    return complete


if __name__ == "__main__":
    print(main())
