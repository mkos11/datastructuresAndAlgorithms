# https://www.acmicpc.net/problem/14502
# pypy3 제출
from sys import*
from collections import*
input=stdin.readline
def bfs():
    q=deque()
    for vx, vy in virus:
        q.append((vx, vy))
    visit = [[0]*m for _ in range(n)]
    infectionArea = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>m-1 or visit[nx][ny] or board[nx][ny]: continue
            infectionArea += 1
            q.append((nx, ny))
            visit[nx][ny] = 1
    return safetyArea - infectionArea

n, m = map(int,input().split())
board = []
virus = []
#벽 3개 세울거라 안전지역 3개 제외
safetyArea = -3
for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(m):
        if board[i][j] == 0: safetyArea += 1
        elif board[i][j] == 2: virus.append((i, j))
ans = 0
for ix in range(n):
    for iy in range(m):
        for jx in range(n):
            for jy in range(m):
                for kx in range(n):
                    for ky in range(m):
                        if board[ix][iy] or board[jx][jy] or board[kx][ky]: continue
                        board[ix][iy] = board[jx][jy] = board[kx][ky] = 1
                        ans = max(ans, bfs())
                        board[ix][iy] = board[jx][jy] = board[kx][ky] = 0
print(ans)

