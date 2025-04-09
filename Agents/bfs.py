def bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = set()
    
    while queue:
        node, path = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path
        
        for neighbor in graph.edges[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None
