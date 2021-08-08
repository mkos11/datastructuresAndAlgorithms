# https://www.acmicpc.net/problem/11779
# 다익스트라
from sys import *
from heapq import *
input = stdin.readline

def dijkstra(start, end):
    prev = [-1] * (n + 1)
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = []
    heappush(pq, (0, start))
    while pq:
        w, u = heappop(pq)
        if dist[u] != w: continue
        for v, weight in adj[u]:
            if dist[v] > w + weight:
                dist[v] = w + weight
                heappush(pq, (dist[v], v))
                prev[v] = u
    res = []
    v = end
    while 1:
        res.append(v)
        if prev[v] == -1: break
        v = prev[v]
    return res[::-1], dist[end]
INF = int(1e9)
n = int(input())
adj = [[]for _ in range(n+1)]
for i in range(int(input())):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
start, end = map(int, input().split())
res, d = dijkstra(start, end)
print(d, len(res), sep="\n")
print(*res)