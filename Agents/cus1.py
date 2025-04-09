{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import sys\
import math\
\
class Graph:\
    def __init__(self):  # fixed from _init_\
        self.nodes = \{\}\
        self.edges = \{\}\
\
    def add_node(self, node, x, y):\
        self.nodes[node] = (x, y)\
        self.edges[node] = \{\}\
\
    def add_edge(self, start, end, cost):\
        self.edges[start][end] = cost\
        self.edges[end][start] = cost\
\
def parse_file(filename):\
    graph = Graph()\
    with open(filename, 'r') as file:\
        lines = [line.strip() for line in file.readlines() if line.strip()]\
\
    mode = None\
    origin = None\
    destinations = []\
\
    i = 0\
    while i < len(lines):\
        line = lines[i]\
        if line.startswith("Nodes:"):\
            mode = "nodes"\
        elif line.startswith("Edges:"):\
            mode = "edges"\
        elif line.startswith("Origin:"):\
            i += 1\
            while i < len(lines) and lines[i] == "":\
                i += 1\
            origin = int(lines[i]) if i < len(lines) else None\
        elif line.startswith("Destinations:"):\
            i += 1\
            while i < len(lines) and lines[i] == "":\
                i += 1\
            if i < len(lines):\
                destinations = list(map(int, lines[i].replace(" ", "").split(";")))\
        elif mode == "nodes":\
            try:\
                node_id, coords = line.split(":")\
                x, y = map(int, coords.strip().strip("()").replace(" ", "").split(","))\
                graph.add_node(int(node_id), x, y)\
            except ValueError:\
                pass\
        elif mode == "edges":\
            try:\
                edge_data, cost = line.split(":")\
                start, end = map(int, edge_data.strip("()").split(","))\
                graph.add_edge(start, end, int(cost))\
            except ValueError:\
                pass\
        i += 1\
\
    return graph, origin, destinations\
\
# Custom Search 1 - Iterative Deepening DFS\
def cus1(graph, start, goal):\
    def dls(node, goal, depth, path):\
        if depth == 0 and node == goal:\
            return path\
        if depth > 0:\
            for neighbor in sorted(graph.edges[node]):  # ensure ascending order\
                if neighbor not in path:\
                    result = dls(neighbor, goal, depth - 1, path + [neighbor])\
                    if result:\
                        return result\
        return None\
\
    depth = 0\
    while True:\
        result = dls(start, goal, depth, [start])\
        if result:\
            return result\
        depth += 1\
\
# Main program execution\
if __name__ == "__main__":\
    if len(sys.argv) != 3:\
        print("Usage: python cus1.py <filename> IDDFS")\
        sys.exit(1)\
\
    filename = sys.argv[1]\
    method = sys.argv[2].upper()\
\
    if method != "IDDFS":\
        print("This file only supports the CUS1 method: IDDFS")\
        sys.exit(1)\
\
    graph, origin, destinations = parse_file(filename)\
\
    best_path = None\
    best_goal = None\
    for goal in destinations:\
        path = cus1(graph, origin, goal)\
        if path:\
            best_path = path\
            best_goal = goal\
            break  # stop once one destination is found\
\
    if best_path:\
        print(f"\{filename\} \{method\}")\
        print(f"Goal: \{best_goal\}, Nodes Expanded: \{len(best_path)\}")\
        print("Path:", " -> ".join(map(str, best_path)))\
    else:\
        print("No valid path found.")\
}