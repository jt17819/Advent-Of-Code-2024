import numpy as np

def main():
    # with open("Day 04/data.txt", "r") as file:
    #     data = file.read().split("\n")
    data = np.loadtxt("Day 04/data.txt", dtype=str)
    data = np.array([[l for l in line] for line in data])
    # print(data)

    # search = "MAS"
    starts = zip(*np.where(data == "A"))
    total = 0
    for row, col in starts:
        if 1 <= row < len(data) - 1 and 1 <= col < len(data[0]) - 1:
            if (data[row - 1][col - 1] == "M" or data[row + 1][col + 1] == "M") and \
            (data[row - 1][col - 1] == "S" or data[row + 1][col + 1] == "S") and \
            (data[row + 1][col - 1] == "M" or data[row - 1][col + 1] == "M") and \
            (data[row + 1][col - 1] == "S" or data[row - 1][col + 1] == "S"):
                total += 1
    return total


if __name__ == "__main__":
    print(main())
