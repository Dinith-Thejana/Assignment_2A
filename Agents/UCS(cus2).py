# Custom Search 2 - Uniform Cost Search
import heapq


def cus2(graph, start, goal):
    pq = [(0, start, [start])]  # (cost, node, path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path, cost

        for neighbor in graph.edges[node]:
            heapq.heappush(pq, (cost + graph.edges[node][neighbor], neighbor, path + [neighbor]))

    return None, float('inf')