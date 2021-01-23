# https://www.acmicpc.net/problem/4963
from sys import*
setrecursionlimit(10**6)
input = stdin.readline
dd = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def dfs(x, y):
    visit[x][y] = 1
    for dx, dy in dd:
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>m-1 or visit[nx][ny] or not board[nx][ny]: continue
        dfs(nx, ny)
while 1:
    m, n = map(int, input().split())
    if n==0 and m==0: break
    board = [list(map(int,input().split())) for _ in range(n)]
    visit = [[0]*m for _ in range(n)]
    island = 0
    for i in range(n):
        for j in range(m):
            if not visit[i][j] and board[i][j]:
                island += 1
                dfs(i, j)
    print(island)
