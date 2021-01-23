# https://www.acmicpc.net/problem/11724
from sys import*
setrecursionlimit(10**6)
input = stdin.readline
def dfs(u):
    visit[u] = 1
    for v in adj[u]:
        if not visit[v]:
            dfs(v)
n, m = map(int, input().split())
adj = [[]for _ in range(n)]
visit = [0] * n
for i in range(m):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    adj[u].append(v)
    adj[v].append(u)
component = 0
for i in range(n):
    if not visit[i]:
        component += 1
        dfs(i)
print(component)