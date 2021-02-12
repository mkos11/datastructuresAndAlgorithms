# adjacency list
class Graph:
    def __init__(self):
        self.adj = dict()

    def edgeAdd(self, u, v):
        if u not in self.adj:
            self.adj[u] = set()
        self.adj[u].add(v)

    def edgeRemove(self, u, v):
        if u not in self.adj or v not in self.adj[u]: return False
        self.adj[u].remove(v)
        return True

    def clear(self):
        self.adj = dict()

    # 연결관계 출력
    def __str__(self):
        res = "연결 관계\n"
        for key, value in self.adj.items():
            for v in value:
                res += f"{key} -> {v}\n"
        return res

if __name__ == "__main__":
    graph = Graph()
    graph.edgeAdd(1, 2)
    graph.edgeAdd(2, 3)
    print(graph)
    graph.clear()
    print(graph)
    graph.edgeAdd(1, 2)
    graph.edgeAdd(1, 2)
    print(graph.edgeRemove(1, 2))
    print(graph.edgeRemove(2, 3))
    graph.edgeAdd(3, 4)
    graph.edgeAdd(4, 3)
    print(graph)
