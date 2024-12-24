import numpy as np


def main():
    with open("Day 07/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 07/data.txt", dtype=str)
    # print(data)
    
    total = 0
    for line in data:
        target, nums = line.split(": ")
        target = int(target)
        nums = [int(n) for n in nums.split(" ")]
        if find_operations(target, nums[1:], nums[0]):
            total += target

    return total


def find_operations(target, nums, curr):
    if not nums:
        return curr == target
    
    return find_operations(target, nums[1:], curr + nums[0]) or \
        find_operations(target, nums[1:], curr * nums[0]) or \
        find_operations(target, nums[1:], int(str(curr) + str(nums[0])))


if __name__ == "__main__":
    print(main())
