# https://www.acmicpc.net/problem/4195
# union_find
from sys import*
input = lambda:stdin.readline().rstrip()
class Node:
    def __init__(self, value):
        self.value = value
        self.cnt = 1
class UnionFind:
    def __init__(self):
        self.parent = {}
    def find(self, u):
        if u not in self.parent: self.parent[u] = Node(u)
        elif self.parent[u].value == u: return u
        else:
            self.parent[u].value = self.find(self.parent[u].value)
        return self.parent[u].value
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v: return self.parent[u].cnt
        self.parent[u].cnt += self.parent[v].cnt
        self.parent[v].value = self.parent[u].value
        return self.parent[u].cnt

for tc in range(int(input())):
    union_find = UnionFind()
    for i in range(int(input())):
        u, v = map(str, input().split())
        print(union_find.union(u, v))