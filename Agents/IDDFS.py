def cus1(graph, start, goal):
    def dls(node, goal, depth, path):
        if depth == 0 and node == goal:
            return path
        if depth > 0:
            for neighbor in sorted(graph.edges[node]):
                if neighbor not in path:
                    result = dls(neighbor, goal, depth - 1, path + [neighbor])
                    if result:
                        return result
        return None

    depth = 0
    while True:
        result = dls(start, goal, depth, [start])
        if result:
            return result
        depth += 1
