class UnionFind():
    def __init__(self):
        self.parent = dict()

    # v가 부모가 됨
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        self.parent[u] = v

    def find(self, u):
        if u not in self.parent: return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def __str__(self):
        res = "child -> parent\n"
        for key, value in self.parent.items():
            res += f"{key} -> {value}\n"
        return res
if __name__ == "__main__":
    unionFind = UnionFind()
    unionFind.union(1, 2)
    unionFind.union(2, 3)
    print(unionFind.find(1))
    print(unionFind.find(2))
    print(unionFind.find(3))
    print(unionFind)