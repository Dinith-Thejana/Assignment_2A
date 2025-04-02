import sys

def parse_input(filename):
    graph = {}
    origin = None
    destinations = []
    with open(filename, 'r') as f:
        section = None
        for line in f:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            if line == "Nodes:":
                section = "nodes"
            elif line == "Edges:":
                section = "edges"
            elif line == "Origin:":
                section = "origin"
            elif line == "Destinations:":
                section = "destinations"
            else:
                if section == "nodes":
                    parts = line.split(':')
                    if len(parts) < 1:
                        continue  # Skip malformed lines
                    node = int(parts[0].strip())
                    graph[node] = []
                elif section == "edges":
                    if ':' not in line:
                        print(f"Warning: Skipping malformed edge line: {line}")
                        continue
                    edge_part, cost_part = line.split(':', 1)  # Ensure at least two parts
                    edge_part = edge_part.strip("() ")
                    nodes = edge_part.split(',')
                    if len(nodes) != 2:
                        print(f"Warning: Skipping malformed edge definition: {line}")
                        continue
                    try:
                        from_node = int(nodes[0].strip())
                        to_node = int(nodes[1].strip())
                        cost = int(cost_part.strip())
                    except ValueError:
                        print(f"Warning: Skipping invalid edge entry: {line}")
                        continue
                    if from_node not in graph:
                        graph[from_node] = []
                    graph[from_node].append((to_node, cost))  # Store (node, cost)
                elif section == "origin":
                    try:
                        origin = int(line.strip())
                    except ValueError:
                        print(f"Warning: Invalid origin value: {line}")
                        origin = None
                elif section == "destinations":
                    try:
                        destinations = [int(x.strip()) for x in line.split(';') if x.strip()]
                    except ValueError:
                        print(f"Warning: Invalid destinations format: {line}")
                        destinations = []
    return graph, origin, destinations

def dfs(graph, origin, destinations):
    stack = [(origin, [origin])]
    visited = set()
    nodes_created = 1
    while stack:
        current_node, path = stack.pop()
        if current_node in destinations:
            return (current_node, nodes_created, path)
        if current_node not in visited:
            visited.add(current_node)
            # Extract neighbor nodes (ignore costs for DFS)
            neighbors = [neighbor for neighbor, _ in graph.get(current_node, [])]
            neighbors_sorted = sorted(neighbors)  # Sort ascending
            for neighbor in reversed(neighbors_sorted):  # Maintain order
                nodes_created += 1
                stack.append((neighbor, path + [neighbor]))
    return (None, nodes_created, [])

if __name__ == "__main__":
    filename = sys.argv[1]
    method = sys.argv[2]
    graph, origin, destinations = parse_input(filename)
    if method == "DFS":
        goal, nodes_created, path = dfs(graph, origin, destinations)
        if goal:
            print(f"{goal} {nodes_created}")
            print(" ".join(map(str, path)))
        else:
            print("No path found")
