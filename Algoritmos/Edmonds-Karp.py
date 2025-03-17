from collections import deque

class Edge:
    def __init__(self, to, rev, cap):
        self.to = to
        self.rev = rev
        self.cap = cap

def add_edge(graph, u, v, cap):
    graph[u].append(Edge(v, len(graph[v]), cap))
    graph[v].append(Edge(u, len(graph[u]) - 1, 0))

def max_flow(graph, source, sink):
    flow = 0
    while True:
        parent = [None] * len(graph)
        queue = deque([source])
        parent[source] = -1 
        
        while queue:
            u = queue.popleft()
            for edge in graph[u]:
                if parent[edge.to] is None and edge.cap > 0:
                    parent[edge.to] = (u, edge)
                    queue.append(edge.to)
                    if edge.to == sink:
                        break  
            else:
                continue
            break  
        
        if parent[sink] is None:  
            break
        
        path_flow = float('inf')
        v = sink
        while v != source:
            u, edge = parent[v]
            path_flow = min(path_flow, edge.cap)
            v = u
        
        v = sink
        while v != source:
            u, edge = parent[v]
            edge.cap -= path_flow
            graph[edge.to][edge.rev].cap += path_flow
            v = u
        
        flow += path_flow
    
    return flow

if __name__ == "__main__":
    n = 4
    graph = [[] for _ in range(n)]
    
    add_edge(graph, 0, 1, 3)
    add_edge(graph, 0, 2, 2)
    add_edge(graph, 1, 2, 5)
    add_edge(graph, 1, 3, 2)
    add_edge(graph, 2, 3, 3)
    
    source = 0
    sink = 3
    
    print("Maximum flow:", max_flow(graph, source, sink)) 