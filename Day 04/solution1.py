import numpy as np

def main():
    # with open("Day 04/data.txt", "r") as file:
    #     data = file.read().split("\n")
    data = np.loadtxt("Day 04/data.txt", dtype=str)
    data = np.array([[l for l in line] for line in data])
    # print(data)

    search = "XMAS"
    starts = zip(*np.where(data == search[0]))
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    total = 0
    for start in starts:
        for d in dirs:
            total += word_search(data, start, d, search, 1, 0)

    return total


def word_search(grid, pos, d, search_word, idx, count):
    if idx == len(search_word):
        return count + 1
    row, col = pos[0] + d[0], pos[1] + d[1]
    
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        if grid[row][col] == search_word[idx]:
            count = word_search(grid, (row, col), d, search_word, idx + 1, count)

    return count

if __name__ == "__main__":
    print(main())
