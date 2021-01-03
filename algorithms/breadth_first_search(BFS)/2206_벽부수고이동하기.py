# https://www.acmicpc.net/problem/2206
from sys import*
from collections import*
input = lambda:stdin.readline().strip()
INF=int(1e9)
def bfs():
    n, m = map(int,input().split())
    board=[list(input())for _ in range(n)]
    visit = [[[INF]*2 for _ in range(m)] for _ in range(n)]
    q=deque()
    q.append((0, 0, 0))
    visit[0][0][0]=1
    while q:
        x, y, k = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>m-1:continue
            if board[nx][ny] == '1' and k < 1 and visit[nx][ny][k+1]==INF:
                q.append((nx, ny, k+1))
                visit[nx][ny][k+1] = visit[x][y][k]+1
            if board[nx][ny] == '0' and visit[nx][ny][k]==INF:
                q.append((nx, ny, k))
                visit[nx][ny][k] = visit[x][y][k]+1
    res = min(visit[n-1][m-1])
    return res if res != INF else -1
print(bfs())