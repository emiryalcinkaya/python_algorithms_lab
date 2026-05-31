"""
Traverse a graph using Depth First Search (DFS).
"""

def dfs(graph, start):

    visited = []
    stack = [start]

    while stack:

        node = stack.pop()

        if node not in visited:
            visited.append(node)

            for neighbor in graph[node]:
                stack.append(neighbor)

    return visited

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

print(dfs(graph, "A"))