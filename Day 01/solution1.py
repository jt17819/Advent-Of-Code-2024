import numpy as np

def main():
    data = np.loadtxt("Day 01/data.txt", dtype=int)
    # print(data)

    a, b = zip(*data)
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()

    distance = 0
    for i in range(len(a)):
        distance += abs(a[i] - b[i])

    return distance

if __name__ == "__main__":
    print(main())
