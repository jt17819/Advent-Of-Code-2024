import numpy as np
from collections import deque


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
    corrected = []
    for instruction in instructions:
        instruction = instruction.split(",")
        book = set()
        check = True
        for page in instruction:
            for rule in rule_dict.get(page, []):
                if rule in book:
                    check = False
            if not check:
                corrected.append(order_instructions(instruction, rule_dict))
                break
            book.add(page)

    for instruction in corrected:
        total += int(instruction[len(instruction) // 2])
    return total


def order_instructions(instruction, rule_dict):
    queue = deque(instruction)
    ordered_book = []
    while queue:
        page = queue.pop()
        check = True
        for rule in rule_dict.get(page, []):
            if rule in queue:
                check = False
                queue.appendleft(page)
                break
        if check:
            ordered_book.append(page)

    return ordered_book


if __name__ == "__main__":
    print(main())
