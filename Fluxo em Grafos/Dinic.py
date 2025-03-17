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
    n = len(graph)
    flow = 0

    while True:
        level = [-1] * n
        level[source] = 0
        queue = deque([source])

        while queue:
            u = queue.popleft()
            for edge in graph[u]:
                if edge.cap > 0 and level[edge.to] == -1:
                    level[edge.to] = level[u] + 1
                    queue.append(edge.to)
                    if edge.to == sink:
                        break

        if level[sink] == -1:
            return flow

        ptr = [0] * n
        while True:
            pushed = dfs(source, sink, float('inf'), level, ptr, graph)
            if pushed == 0:
                break
            flow += pushed


def dfs(u, sink, limit, level, ptr, graph):
    if u == sink:
        return limit

    total_pushed = 0
    while ptr[u] < len(graph[u]) and total_pushed < limit:
        edge = graph[u][ptr[u]]

        if edge.cap > 0 and level[u] + 1 == level[edge.to]:
            res = dfs(edge.to, sink, min(
                limit - total_pushed, edge.cap), level, ptr, graph)
            if res > 0:
                edge.cap -= res
                graph[edge.to][edge.rev].cap += res
                total_pushed += res

            ptr[u] += 1
        else:
            ptr[u] += 1

    return total_pushed


if __name__ == "__main__":
    n = 4
    graph = [[] for _ in range(n)]

    # Adiciona arestas
    add_edge(graph, 0, 1, 3)
    add_edge(graph, 0, 2, 2)
    add_edge(graph, 1, 2, 5)
    add_edge(graph, 1, 3, 2)
    add_edge(graph, 2, 3, 3)

    source = 0
    sink = 3

    print("Fluxo máximo:", max_flow(graph, source, sink))
