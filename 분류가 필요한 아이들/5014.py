# https://www.acmicpc.net/problem/5014
# bfs
from collections import*
def bfs():
    visit = {s: 0}
    q = deque()
    q.append(s)
    while q:
        x = q.popleft()
        if x == g: return visit[x]
        for nx in [x+u, x-d]:
            if nx in visit: continue
            if nx < 1 or nx > f: continue
            visit[nx] = visit[x] + 1
            q.append(nx)
    return 'use the stairs'
f, s, g, u, d = map(int, input().split())
print(bfs())