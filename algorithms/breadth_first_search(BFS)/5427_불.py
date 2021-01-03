# https://www.acmicpc.net/problem/3055
from sys import*
from collections import*
input=lambda:stdin.readline().strip()
def bfs():
    m, n = map(int,input().split())
    board = []
    sx, sy = 0, 0
    q=deque()
    for i in range(n):
        board.append(list(input()))
        for j in range(m):
            if board[i][j] == '@':
                sx, sy = i, j
            elif board[i][j] == '*':
                q.append((i, j, 0))
    q.append((sx, sy, 0))
    while q:
        x, y, time = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>m-1:
                if board[x][y] == '@': return time+1
                else: continue
            if board[nx][ny]!='.': continue
            q.append((nx, ny, time+1))
            board[nx][ny] = board[x][y]
    return 'IMPOSSIBLE'
for tc in range(int(input())):
    print(bfs())