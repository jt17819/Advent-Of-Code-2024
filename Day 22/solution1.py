import numpy as np


def main():
    # with open("Day 22/data.txt", "r") as file:
    #     data = file.read().split("\n")
    data = np.loadtxt("Day 22/data.txt", dtype=int)
    # print(data)

    interations = range(2000)
    total = 0
    for num in data:
        for _ in interations:
            num ^= (num << 6)
            num &= 16777215
            num ^= (num >> 5)
            num &= 16777215
            num ^= (num << 11)
            num &= 16777215
        total += num

    return total


if __name__ == "__main__":
    print(main())
