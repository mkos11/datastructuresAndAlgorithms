# https://www.acmicpc.net/problem/11780
from sys import*
from collections import*
input = stdin.readline

def location(u, v):
    res = deque()
    if nxt[u][v] == -1:
        print(0)
        return
    while True:
        if nxt[u][v] == -1: break
        res.append(v+1)
        v = nxt[u][v]
    res.reverse()
    res.appendleft(u+1)
    print(len(res), *res)

INF = int(1e18)
n = int(input())
dist = [[INF]*n for _ in range(n)]
nxt = [[-1]*n for _ in range(n)]
for u in range(int(input())):
    u, v, w = map(int, input().split())
    u-=1; v-=1
    if dist[u][v] > w:
        dist[u][v] = w
        nxt[u][v] = u
for u in range(n): dist[u][u] = 0
for k in range(n):
    for u in range(n):
        for v in range(n):
            if dist[u][v] > dist[u][k] + dist[k][v]:
                dist[u][v] = dist[u][k] + dist[k][v]
                nxt[u][v] = nxt[k][v]
for u in range(n):
    for v in range(n):
        print(dist[u][v] if dist[u][v] != INF else 0, end=' ')
    print()

for u in range(n):
    for v in range(n):
        location(u, v)