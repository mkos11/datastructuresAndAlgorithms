# https://www.acmicpc.net/problem/14500
# pypy3 제출
from sys import*
input=stdin.readline
dd=[(0, 1), (0, -1), (1, 0), (-1, 0)]
def dfs(x, y, pos, SUM):
    res = 0
    visit[x][y]=1
    if pos == 4: return SUM
    for dx, dy in dd:
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>m-1 or visit[nx][ny]: continue
        visit[nx][ny]=1
        res = max(res, dfs(nx, ny, pos+1, SUM+board[nx][ny]))
        visit[nx][ny]=0
    visit[x][y]=0
    return res
def TShape(x, y):
    res = []
    for dx, dy in dd:
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>m-1: continue
        res.append(board[nx][ny])
    if len(res) == 4: return board[x][y] + sum(res) - min(res)
    return board[x][y] + sum(res)
n,m=map(int,input().split())
board=[list(map(int,input().split()))for _ in range(n)]
visit=[[0]*m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dfs(i, j, 0, 0), TShape(i, j))
print(ans)