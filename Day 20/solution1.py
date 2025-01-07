import numpy as np


def main():
    with open("Day 20/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 20/data.txt", dtype=str)
    data = np.array([[char for char in line] for line in data], dtype="<U7")
    # print(data)
    
    start = list(zip(*np.where(data == "S")))[0]
    end = list(zip(*np.where(data == "E")))[0]
    # print(start, end)
    data[end] = "."
    
    step = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    pos = start
    
    data[pos] = step
    visited = set([start])
    while pos != end:
        for d in dirs:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if data[new_pos] == ".":
                pos = new_pos
                step += 1
                break

        data[pos] = step
        visited.add(pos)
    
    cheat_dirs = [(-2, 0), (0, 2), (2, 0), (0, -2)]
    counter = {}
    for pos in visited:
        for d in cheat_dirs:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if 0 <= new_pos[0] < len(data) and 0 <= new_pos[1] < len(data[0]) and data[new_pos] != "#" and int(data[new_pos]) > int(data[pos]):
                time_saved = int(data[new_pos]) - int(data[pos]) - 2
                counter[time_saved] = counter.get(time_saved, 0) + 1

    time_skips = list(sorted(counter.items(), key=lambda x:x[0]))
    
    return sum(t[1] for t in time_skips if t[0] >= 100)


if __name__ == "__main__":
    print(main())
