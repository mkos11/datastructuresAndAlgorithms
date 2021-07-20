# https://www.acmicpc.net/problem/15591
# graph
from sys import*
from collections import*
input = stdin.readline
n, m = map(int, input().split())
adj = [[]for _ in range(n+1)]
for i in range(n-1):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
res = []
for i in range(m):
    visit = [False] * (n + 1)
    k, s = map(int, input().split())
    cnt = 0
    q = deque()
    q.append(s)
    visit[s] = True
    while q:
        u = q.popleft()
        for v, w in adj[u]:
            if visit[v]: continue
            if w >= k:
                cnt += 1
                visit[v] = True
                q.append(v)
    res.append(cnt)
print(*res, sep="\n")