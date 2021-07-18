# https://www.acmicpc.net/problem/17616
# graph
from collections import *
from sys import *
input = stdin.readline
def solve(u, adj):
    q = deque()
    q.append(u)
    visit = [False]*(n+1)
    visit[u] = True
    cnt = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if visit[v]: continue
            visit[v] = True
            q.append(v)
            cnt += 1
    return cnt

n, m, start = map(int,input().split())
prev = [[]for _ in range(n+1)]
nxt = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int,input().split())
    prev[v].append(u)
    nxt[u].append(v)
print(solve(start, prev) + 1, n - solve(start, nxt))
