import numpy as np


def check_safe(report):
    diffs = [report[i] - report[i-1] for i in range(1, len(report))]
    if report[0] < report[1]:
        check = range(1,4)
    else:
        check = range(-3,0)
    return (all(diff in check for diff in diffs))


def main():
    with open("Day 02/data.txt", "r") as file:
        data = file.read().split("\n")
    # print(data)

    safe_count = 0
    for report in data:
        report = np.array(report.split(" "), dtype=int)
        
        if check_safe(report):
            safe_count += 1
        else:
            for i in range(len(report)):
                new_report = np.delete(report, i)
                if check_safe(new_report):
                    safe_count += 1
                    break

    return safe_count

if __name__ == "__main__":
    print(main())

