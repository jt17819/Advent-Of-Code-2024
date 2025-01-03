import numpy as np
from collections import deque


def main():
    with open("Day 16/data.txt", "r") as file:
        data = file.read().split("\n")
    data = np.array([[char for char in line] for line in data])
    # print(data)

    start = next(zip(*np.where(data == "S")))
    end = next(zip(*np.where(data == "E")))
    # print(start, end)

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_dir = (0, 1)
    open_nodes = deque([(start, curr_dir, 0)])
    score_array = np.full_like(data, 10000000, dtype=int)

    while open_nodes:
        node, curr_dir, score = open_nodes.popleft()

        if data[node] == "#" or score_array[node] < score:
            continue

        score_array[node] = score
        for d in dirs:
            new_node = (node[0] + d[0], node[1] + d[1])
            if d == curr_dir:
                open_nodes.append((new_node, d, score + 1))
            else:
                open_nodes.append((new_node, d, score + 1001))

    # print(score_array)
    # print(score_array[end])
    ans = backtrack_bfs(score_array)
    
    return ans


def turn_right(cur_dir):
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    return directions[(directions.index(cur_dir) + 1 + len(directions)) % len(directions)]


def turn_left(cur_dir):
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    return directions[(directions.index(cur_dir) - 1 + len(directions)) % len(directions)]


def backtrack_bfs(cost_map):
    queue = deque()
    total = 1
    start_1 = (1, len(cost_map[1]) - 2, (1, 0), cost_map[1][len(cost_map[1]) - 2])
    start_2 = (1, len(cost_map[1]) - 2, (0, -1), cost_map[1][len(cost_map[1]) - 2])
    queue.append(start_1)
    queue.append(start_2)
    visited = set()

    while queue:
        cur_x, cur_y, cur_dir, cur_score = queue.popleft()

        allowed_directions_n_score = [
            (cur_dir, cur_score - 1),
            (turn_left(cur_dir), cur_score - 1001),
            (turn_right(cur_dir), cur_score - 1001)
        ]

        for new_dir, new_score in allowed_directions_n_score:
            new_x, new_y = cur_x + new_dir[0], cur_y + new_dir[1]
            if cost_map[new_x][new_y] in [new_score, new_score - 1000] and (new_x, new_y) not in visited:
                total += 1
                queue.append((new_x, new_y, new_dir, new_score))
                visited.add((new_x, new_y))

    return total


if __name__ == "__main__":
    print(main())
