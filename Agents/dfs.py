def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path
        
        for neighbor in graph.edges[node]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    
    return None
