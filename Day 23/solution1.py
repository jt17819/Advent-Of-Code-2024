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

    total = set()
    for comp in t_comps:
        total |= connected_comps(graph, comp, [])

    return len(total)


def connected_comps(graph, node, path):
    if node in path:
        return set()
    path.append(node)
    if len(path) == 3:
        if path[0] in graph[node]:
            return set([",".join(sorted(path))])
        else:
            return set()
    
    paths = set()
    for connection in graph[node]:
        paths |= connected_comps(graph, connection, path[:])

    return paths


if __name__ == "__main__":
    print(main())
