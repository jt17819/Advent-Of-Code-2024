import numpy as np

def main():
    with open("Day 02/data.txt", "r") as file:
        data = file.read().split("\n")
    # print(data)

    safe_count = 0
    for report in data:
        report = np.array(report.split(" "), dtype=int)
        if report[0] < report[1]:
            check = range(1,4)
        else:
            check = range(-3,0)
        safe = True

        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            if diff not in check:
                safe = False
                break
        if safe:
            safe_count += 1

    return safe_count

if __name__ == "__main__":
    print(main())
