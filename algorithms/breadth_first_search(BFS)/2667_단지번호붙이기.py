# https://www.acmicpc.net/problem/2667
from sys import*
from collections import*
input = lambda: stdin.readline().strip()
def bfs(x, y):
    visit[x][y] = 1
    q = deque()
    q.append((x, y))
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visit[nx][ny] or board[nx][ny]!='1': continue
            q.append((nx, ny))
            visit[nx][ny] = 1
            cnt += 1
    return cnt
n = int(input())
board = [list(input())for _ in range(n)]
visit = [[0] * n for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if board[i][j] == '1' and not visit[i][j]:
            res.append(bfs(i, j))
res.sort()
print(len(res))
for r in res: print(r)