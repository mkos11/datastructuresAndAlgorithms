# https://www.acmicpc.net/problem/1012
from sys import*
from collections import*
input = stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>m-1 or visit[nx][ny] or not board[nx][ny]: continue
            visit[nx][ny] = 1
            q.append((nx, ny))

for tc in range(int(input())):
    m, n, k = map(int,input().split())
    board = [[0] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    for i in range(k):
        y, x = map(int,input().split())
        board[x][y] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visit[i][j] and board[i][j]:
                cnt += 1
                bfs(i, j)
    print(cnt)

