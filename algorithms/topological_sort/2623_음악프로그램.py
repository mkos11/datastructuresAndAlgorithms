from sys import*
from collections import*
input=stdin.readline

def tSort():
    res = []
    q = deque()
    for i in range(n):
        if not indegree[i]:
            q.append(i)
    for i in range(n):
        if not q:
            print(0)
            return
        u = q.popleft()
        res.append(str(u+1))
        for v in adj[u]:
            indegree[v]-=1
            if not indegree[v]:
                q.append(v)
    print("\n".join(res))
n, m = map(int,input().split())
adj = [[]for _ in range(n)]
indegree = [0] * n
for i in range(m):
    info = list(map(int,input().split()))
    for v in range(1, len(info)-1):
        adj[info[v]-1].append(info[v+1]-1)
        indegree[info[v+1]-1] += 1
tSort()
