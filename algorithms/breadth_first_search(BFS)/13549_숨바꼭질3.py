from sys import*
from collections import*
input = stdin.readline

def bfs():
    visit[n] = 0
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        nx = x * 2
        if 0 <= nx < MAX:
            if visit[nx] == -1 or (visit[x] < visit[nx] and visit[nx] != -1):
                visit[nx] = visit[x]
                q.append(nx)
        # x-1, x+1 순서 바꿔야지 성공뜸.. 반례 존재하나봐 와;;; 당연히 bfs() 깊이로 같을줄
        for nx in [x-1, x+1]:
            if 0 <= nx < MAX and visit[nx] == -1:
                q.append(nx)
                visit[nx] = visit[x] + 1
MAX = int(1e5+1)
n, k = map(int, input().split())
visit = [-1] * MAX
bfs()
print(visit[k])