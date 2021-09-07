# https://www.acmicpc.net/problem/17244
from itertools import *
from collections import *
def bfs(x, y, dest_x, dest_y):
    visit = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visit[x][y] = 0
    while q:
        x, y = q.popleft()
        if x == dest_x and y == dest_y: return x, y, visit[x][y]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1 or board[nx][ny] == '#' or visit[nx][ny] != -1: continue
            visit[nx][ny] = visit[x][y] + 1
            q.append((nx, ny))
    return x, y, -1
def solve(orders):
    res = 0
    x, y = sx, sy
    for ox, oy in orders:
        x, y, dist = bfs(x, y, ox, oy)
        if dist == -1: return INF
        res += dist
    res += bfs(x, y, ex, ey)[2]
    return res
INF = int(1e9)
m, n = map(int, input().split())
sx, sy, ex, ey = -1, -1, -1, -1
board = [list(input()) for _ in range(n)]
items = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'X':
            items.append((i, j))
        elif board[i][j] == 'S':
            sx, sy = i, j
        elif board[i][j] == 'E':
            ex, ey = i, j
res = INF
for orders in permutations(items):
    res = min(res, solve(orders))
print(res)