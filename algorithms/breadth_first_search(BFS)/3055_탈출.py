from sys import*
from collections import*
input=lambda:stdin.readline().strip()
def bfs():
    n, m = map(int, input().split())
    board=[]
    sx, sy = -1, -1
    q=deque()
    for i in range(n):
        board.append(list(input()))
        for j in range(m):
            if board[i][j] == 'S':
                sx, sy = i, j
            elif board[i][j] == '*':
                q.append((i, j, 0))
    q.append((sx, sy, 0))
    while q:
        x, y, time = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>m-1: continue
            if board[nx][ny] == 'D' and board[x][y]=='S': return time+1
            if board[nx][ny] == '.':
                q.append((nx, ny, time+1))
                board[nx][ny] = board[x][y]
    return "KAKTUS"
print(bfs())