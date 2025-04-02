import heapq

def gbfs(graph, start, goal):
    pq = [(graph.heuristic(start, goal), start, [start])]
    visited = set()

    while pq:
        _, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path

        for neighbor in graph.edges[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (graph.heuristic(neighbor, goal), neighbor, path + [neighbor]))

    return None

#kahbv;kjaenvj
