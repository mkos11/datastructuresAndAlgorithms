# https://www.acmicpc.net/problem/2178
from sys import*
from collections import*
input=lambda:stdin.readline().strip()
def bfs():
    visit=[[0]*m for _ in range(n)]
    q=deque()
    q.append((0,0))
    visit[0][0]=1
    while q:
        x, y = q.popleft()
        if x==n-1 and y==m-1: return visit[x][y]
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>m-1 or visit[nx][ny] or board[nx][ny]=='0': continue
            q.append((nx, ny))
            visit[nx][ny]=visit[x][y]+1
    return -1

n, m = map(int,input().split())
board=list(input()for _ in range(n))

print(bfs())