import numpy as np


def main():
    # with open("Day 12/data.txt", "r") as file:
    #     data = file.read().split("\n")
    data = np.loadtxt("Day 12/data.txt", dtype=str)
    data = np.array([[l for l in line] for line in data])
    # print(data)
    
    letters = np.unique(data)
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    total = 0
    for letter in letters:
        locations = set(zip(*np.where(data == letter)))

        while locations:
            region = []
            open_pos = [next(iter(locations))]
            perimeter = 0

            while open_pos:
                pos = open_pos.pop()
                locations.remove(pos)
                region.append(pos)
                perimeter += 4

                for d in dirs:
                    new_pos = (pos[0] + d[0], pos[1] + d[1])
                    if new_pos in locations:
                        if new_pos not in open_pos:
                            open_pos.append(new_pos)
                        perimeter -= 2

            total += count_sides(region) * len(region)

    return total


def count_sides(region):
    count = 0
    for pos in region:
        '''
        012
        345
        678
        '''
        area = [(pos[0] - 1,pos[1] - 1), (pos[0] - 1,pos[1]), (pos[0] - 1,pos[1] + 1),
                (pos[0],pos[1] - 1), (pos[0],pos[1]), (pos[0],pos[1] + 1),
                (pos[0] + 1,pos[1] - 1), (pos[0] + 1,pos[1]), (pos[0] + 1,pos[1] + 1)]
        
        adjacent = (area[1] in region) + (area[3] in region) + (area[5] in region) + (area[7] in region)
        #alone
        if adjacent == 0:
            count += 4
        
        #end
        elif adjacent == 1:
            count += 2

        #concave corners
        if area[1] in region and area[3] in region and area[0] not in region:
            count += 1
        if area[1] in region and area[5] in region and area[2] not in region:
            count += 1
        if area[7] in region and area[5] in region and area[8] not in region:
            count += 1
        if area[7] in region and area[3] in region and area[6] not in region:
            count += 1

        #convex corners
        if area[1] in region and area[3] in region and area[5] not in region and area[7] not in region:
            count += 1
        if area[1] in region and area[5] in region and area[3] not in region and area[7] not in region:
            count += 1
        if area[7] in region and area[5] in region and area[1] not in region and area[3] not in region:
            count += 1
        if area[7] in region and area[3] in region and area[5] not in region and area[1] not in region:
            count += 1

    return count


if __name__ == "__main__":
    print(main())
