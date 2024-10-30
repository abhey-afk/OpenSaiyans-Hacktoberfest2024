# Depth-First Search using recursion
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set if not passed
    
    # Mark the current node as visited
    visited.add(start)
    print(start, end=' ')  # Process the node (e.g., print it)

    # Recur for all the adjacent nodes
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

