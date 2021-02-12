# 트으리이
# 1. 연결그래프(컴포넌트가 하나)
# 2. 방향을 무시하였을 때, 싸이클이 존재하지 않음(그러려면 자연스레 간선 개수는 정점 - 1개가 됨)

# 어떤식으로 구현해보지? 루트 안정해진 트리 BFS, DFS로 탐색하는거?
from collections import*

class Tree:
    def __init__(self):
        self.adj = dict()

    def edgeAdd(self, u, v):
        if u not in self.adj:
            self.adj[u] = set()
        if v not in self.adj:
            self.adj[v] = set()
        self.adj[u].add(v)
        self.adj[v].add(u)

    def edgeRemove(self, u, v):
        if u not in self.adj or v not in self.adj[u] or v not in self.adj or u not in self.adj[v]: return False
        self.adj[u].remove(v)
        self.adj[v].remove(u)
        return True

    # 여러곳 갈 수 있으면 번호 낮은곳부터 방문하도록 sorted 달아줌
    def DFS(self, root):
        print(f"DFS, root:{root}")
        visit = {}
        def _DFS(u):
            if u not in visit:
                visit[u] = True
                print(f"{u}", end=" ")
            for v in sorted(self.adj[u]):
                if v not in visit:
                    _DFS(v)
        _DFS(root)
        print()

    def BFS(self, root):
        print(f"BFS, root:{root}")
        visit = {}
        q = deque([root])
        visit[root] = True
        while q:
            u = q.popleft()
            print(f"{u}", end=" ")
            for v in sorted(self.adj[u]):
                if v not in visit:
                    visit[v] = True
                    q.append(v)
        print()

if __name__ == "__main__":
    tree = Tree()
    tree.edgeAdd(1, 2)
    tree.edgeAdd(1, 8)
    tree.edgeAdd(2, 3)
    tree.edgeAdd(2, 4)
    tree.edgeAdd(4, 5)
    tree.edgeAdd(5, 6)
    tree.edgeAdd(5, 7)
    tree.DFS(1)
    tree.BFS(1)
    tree.DFS(4)
    print(tree.edgeRemove(5, 7))
    print(tree.edgeRemove(5, 7))
    tree.BFS(1)