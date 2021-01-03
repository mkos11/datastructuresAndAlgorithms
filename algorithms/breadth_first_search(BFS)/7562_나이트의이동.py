# https://www.acmicpc.net/problem/7562
from sys import*
from collections import*
input=stdin.readline
move = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
def bfs(sx, sy, ex, ey, n):
    q=deque()
    q.append((sx, sy))
    visit=[[-1]*n for _ in range(n)]
    visit[sx][sy]=0
    while q:
        x, y = q.popleft()
        if x==ex and y==ey: return visit[x][y]
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visit[nx][ny]!=-1: continue
            q.append((nx, ny))
            visit[nx][ny]=visit[x][y]+1
    return -1
for tc in range(int(input())):
    n = int(input())
    sx, sy = map(int,input().split())
    ex, ey = map(int,input().split())
    print(bfs(sx, sy, ex, ey, n))
