# https://www.acmicpc.net/problem/2468
from sys import*
setrecursionlimit(10**6)
input = stdin.readline
def dfs(x, y, height):
    visit[x][y] = 1
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visit[nx][ny] or board[nx][ny] <= height: continue
        dfs(nx, ny, height)
n = int(input())
board = [list(map(int, input().split()))for _ in range(n)]
maxHeight = 0
for i in range(n):
    for j in range(n):
        maxHeight = max(maxHeight, board[i][j])
maxSafeArea = 0
for height in range(maxHeight):
    safeArea = 0
    visit = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visit[x][y] and board[x][y] > height:
                dfs(x, y, height)
                safeArea += 1
    maxSafeArea = max(maxSafeArea, safeArea)
print(maxSafeArea)