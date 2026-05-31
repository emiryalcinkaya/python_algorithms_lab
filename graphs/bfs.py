"""
Traverse a graph using Breadth First Search (BFS).
"""

def bfs(graph, start):

    visited = []
    queue = [start]

    while queue:

        node = queue.pop(0)

        if node not in visited:
            visited.append(node)

            for neighbor in graph[node]:
                queue.append(neighbor)

    return visited

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

print(bfs(graph, "A"))