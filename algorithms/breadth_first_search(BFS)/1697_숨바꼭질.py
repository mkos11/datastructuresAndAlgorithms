# https://www.acmicpc.net/problem/1697
from collections import*
x, k = map(int,input().split())
q=deque()
q.append(x)
MAX = int(1e5)+1
visit=[-1]*MAX
visit[x] = 0
while q:
    x = q.popleft()
    if x == k:
        print(visit[x])
        exit()
    for nx in [x*2, x+1, x-1]:
        if nx >= MAX or nx < 0 or visit[nx]!=-1: continue
        q.append(nx)
        visit[nx] = visit[x]+1
