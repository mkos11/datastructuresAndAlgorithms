# https://www.acmicpc.net/problem/13460
from sys import*
from collections import*
input=lambda:stdin.readline().strip()
def move(x, y, dx, dy, board):
    moveDist = 0
    while 1:
        x, y = x+dx, y+dy
        moveDist += 1
        if board[x][y] == '#': return (x-dx, y-dy, moveDist-1)
        if board[x][y] == 'O': return (x, y, moveDist)
def bfs():
    n, m = map(int,input().split())
    visit=[[[[-1]*m for _ in range(n)]for _ in range(m)]for _ in range(n)]
    board=[]
    rx, ry, bx, by = -1, -1, -1, -1
    for i in range(n):
        board.append(input())
        for j in range(m):
            if board[i][j] == 'R': rx, ry = i, j
            elif board[i][j] == 'B': bx, by = i, j
    q=deque()
    q.append((rx, ry, bx, by))
    visit[rx][ry][bx][by]=0
    while q:
        rx, ry, bx, by = q.popleft()
        if visit[rx][ry][bx][by] > 10: return -1
        if board[rx][ry] == 'O': return visit[rx][ry][bx][by]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nrx, nry, rd = move(rx, ry, dx, dy, board)
            nbx, nby, bd = move(bx, by, dx, dy, board)
            if board[nbx][nby] == 'O': continue
            if nrx == nbx and nry == nby:
                if rd < bd:
                    nbx -= dx
                    nby -= dy
                else:
                    nrx -= dx
                    nry -= dy
            if visit[nrx][nry][nbx][nby] == -1:
                q.append((nrx, nry, nbx, nby))
                visit[nrx][nry][nbx][nby] = visit[rx][ry][bx][by] + 1
    return -1
print(bfs())