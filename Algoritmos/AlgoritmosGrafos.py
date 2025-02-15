from collections import deque

def bfsMatrix(matrix, start):
    n = len(matrix)
    visited = [False] * n
    queue = deque([start])
    visited[start] = True
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in range(n):
            if matrix[node][neighbor] and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return order

def dfsMatrix(matrix, start):
    n = len(matrix)
    visited = [False] * n
    order = []
    
    def dfs(node):
        visited[node] = True
        order.append(node)
        for neighbor in range(n):
            if matrix[node][neighbor] and not visited[neighbor]:
                dfs(neighbor)
    
    dfs(start)
    return order

def bfsList(graph, start):
    nodes = set()
    for node in graph:
        nodes.add(node)
        nodes.update(graph[node])
    visited = {node: False for node in nodes}

    if start not in visited:
        return []
    queue = deque([start])
    visited[start] = True
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return order

def dfsList(graph, start):
    nodes = set()
    for node in graph:
        nodes.add(node)
        nodes.update(graph[node])
    visited = {node: False for node in nodes}
    order = []

    if start not in visited:
        return order
    
    def dfs(node):
        visited[node] = True
        order.append(node)

        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                dfs(neighbor)
    
    dfs(start)
    return order