import numpy as np


def main():
    with open("Day 23/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 23/data.txt", dtype=str)
    # print(data)
    
    graph = {}
    t_comps = set()
    all_comps = set()
    for line in data:
        a, b = line.split("-")
        graph[a] = graph.get(a, set()) | set([b])
        graph[b] = graph.get(b, set()) | set([a])

        if a not in all_comps:
            all_comps.add(a)
        if b not in all_comps:
            all_comps.add(b)

        if a[0] == "t" and a[0] not in t_comps:
            t_comps.add(a)
        if b[0] == "t" and b[0] not in t_comps:
            t_comps.add(b)

    ans = set()
    
    for comp in all_comps:
        total = connected_comps(graph, comp, set())
        if len(total) > len(ans):
            ans = total

    # print(list(sorted(total)))
    return ",".join(sorted(ans))


def connected_comps(graph, node, path):
    if node in path:
        return set()

    for prev in path:
        if prev not in graph[node]:
            return set()

    path.add(node)
    paths = set(path)
    for connection in graph[node]:
        paths |= connected_comps(graph, connection, path)
    # print(paths)

    return paths


if __name__ == "__main__":
    print(main())
