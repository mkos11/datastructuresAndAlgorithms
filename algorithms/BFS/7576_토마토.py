# https://www.acmicpc.net/problem/7576
from sys import*
from collections import*
input=stdin.readline
def bfs():
    q=deque()
    goalTomatoCnt=0
    curTomatoCnt=0
    for i in range(n):
        for j in range(m):
            if not board[i][j]: goalTomatoCnt+=1
            elif board[i][j]==1:
                q.append((i, j))
    if goalTomatoCnt==curTomatoCnt: return 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>m-1 or board[nx][ny]!=0: continue
            q.append((nx, ny))
            curTomatoCnt+=1
            board[nx][ny]=board[x][y]+1
            if curTomatoCnt == goalTomatoCnt: return board[x][y]
    return -1

m, n = map(int,input().split())
board=[list(map(int,input().split()))for _ in range(n)]

print(bfs())