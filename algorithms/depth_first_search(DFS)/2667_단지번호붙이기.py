# https://www.acmicpc.net/problem/2667
from sys import*
setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()

def dfs(x, y):
    global cnt
    visit[x][y] = 1
    cnt += 1
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visit[nx][ny] or board[nx][ny]!='1':continue
        visit[nx][ny]=1
        dfs(nx, ny)
n = int(input())
board = [input() for _ in range(n)]
visit = [[0]*n for _ in range(n)]
'''
위 코드
board = []
for i in range(n):
    board.append(input())
랑 같은 코드
'''
res = []
for i in range(n):
    for j in range(n):
        if not visit[i][j] and board[i][j]=='1':
            cnt = 0
            dfs(i, j)
            res.append(cnt)
res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])
