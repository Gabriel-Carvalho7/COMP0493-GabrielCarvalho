from collections import deque, defaultdict

def max_flow(graph, source, sink):
    residual = defaultdict(dict)
    for u in graph:
        for v, cap in graph[u].items():
            residual[u][v] = cap
            residual[v][u] = 0 

    max_flow = 0

    while True:
        parent = {}
        visited = set([source])
        queue = deque([source])
        found = False
        
        while queue:
            u = queue.popleft()
            if u == sink:
                found = True
                break
            for v in residual[u]:
                if v not in visited and residual[u][v] > 0:
                    visited.add(v)
                    parent[v] = u
                    queue.append(v)
        
        if not found:
            break  
        
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u
        
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u
        
        max_flow += path_flow
    return max_flow

if __name__ == "__main__":
    graph = {
        's': {'a': 10, 'b': 2},
        'a': {'b': 4, 't': 8},
        'b': {'t': 9},
        't': {}
    }

    source = 's'
    sink = 't'
    print("Fluxo máximo:", max_flow(graph, source, sink)) 