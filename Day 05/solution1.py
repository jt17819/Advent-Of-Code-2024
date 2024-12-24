import numpy as np


def main():
    with open("Day 05/data.txt", "r") as file:
        data = file.read().split("\n\n")
    # data = np.loadtxt("Day 05/data.txt", dtype=str)
    rules, instructions = data[0].split("\n"), data[1].split("\n")
    # print(rules, instructions)

    rule_dict = {}
    for rule in rules:
        rule = rule.split("|")
        rule_dict[rule[0]] = rule_dict.get(rule[0], []) + [rule[1]]

    total = 0
    for instruction in instructions:
        instruction = instruction.split(",")
        book = set()
        check = True
        for page in instruction:
            for rule in rule_dict.get(page, []):
                if rule in book:
                    check = False
            if not check:
                break
            book.add(page)
        if check:
            total += int(instruction[len(instruction) // 2])

    return total


if __name__ == "__main__":
    print(main())
