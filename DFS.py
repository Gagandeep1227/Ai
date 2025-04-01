graph = {
    'A': set(['B', 'C']), 
    'B': set(['D', 'E']),
    'C': set(['F']),
    'D': set([]),
    'E': set([]),
    'F': set([])
}

def dfs_stack(graph, start):
    stack = [start]
    visited = set()
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current, end=" ")
            visited.add(current)
            stack.extend(sorted(graph[current], reverse=True)) 

print("DFS Traversal:")
dfs_stack(graph, 'A')
