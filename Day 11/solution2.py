import numpy as np


def main():
    # with open("Day 11/data.txt", "r") as file:
    #     data = file.read().split("\n")
    data = np.loadtxt("Day 11/data.txt", dtype=np.int64)
    # print(data)

    d = {}
    for num in data:
        d[num] = d.get(num, 0) + 1

    for _ in range(75):
        d = do_step(d)

    return sum(d.values())


def do_step(nums):
    new_nums = {}
    for stone in nums.keys():
        if stone == 0:
            new_stones = [1]
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            split = str(stone)[:half], str(stone)[half:]
            new_stones = [int(split[0]), int(split[1])]
        else:
            new_stones = [stone * 2024]
        
        for new_stone in new_stones:
            new_nums[new_stone] = new_nums.get(new_stone, 0) + nums[stone]

    return new_nums

if __name__ == "__main__":
    print(main())
