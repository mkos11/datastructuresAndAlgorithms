# https://www.acmicpc.net/problem/1260
from sys import*
from collections import*
input=stdin.readline
def dfs(u):
    global visited
    visited[u] = True
    print(u, end=' ')
    for v in adj[u]:
        if not visited[v]:
            dfs(v)

def bfs(u):
    q=deque()
    q.append(u)
    visited = [False]*n
    visited[u] = True
    while q:
        u = q.popleft()
        print(u, end=' ')
        for v in adj[u]:
            if not visited[v]:
                q.append(v)
                visited[v]=True

n, m, s = map(int,input().split())
n+=1
# connected = {}
connected = [[0] * n for _ in range(n)]
adj = [[]*(n) for _ in range(n)]
for i in range(m):
    #x, y 크기순으로 강제해서 그 쌍으로 중복 제거
    x, y = map(int,input().split())
    if x > y: x, y = y, x
    # dict() 사용해도 되고
    # if (x, y) in connected:
    #     continue
    # connected[(x, y)]=True
    # 이차원 배열로 체크해도 되고
    if connected[x][y]: continue
    connected[x][y] = 1
    adj[x].append(y)
    adj[y].append(x)
for i in range(n):
    adj[i].sort()
visited=[False]*n
dfs(s)
print()
bfs(s)