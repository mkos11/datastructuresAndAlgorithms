# https://www.acmicpc.net/problem/17144
# pypy3 제출
from sys import*
input = stdin.readline
U, R, D, L = (-1, 0), (0, 1), (1, 0), (0, -1)
clockwise = [R, D, L, U]
counterClockwise = [R, U, L, D]
def purify(x, y, directions):
    global board
    temp = 0
    for dx, dy in directions:
        while 1:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>m-1 or board[nx][ny]==-1: break
            temp, board[nx][ny] = board[nx][ny], temp
            x, y = nx, ny
def spread():
    global board
    addBoard = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            spreadCnt = 0
            if board[x][y]!=-1 and board[x][y]:
                for dx, dy in clockwise:
                    nx, ny = x+dx, y+dy
                    if nx<0 or ny<0 or nx>n-1 or ny>m-1 or board[nx][ny]==-1: continue
                    spreadCnt += 1
                    addBoard[nx][ny] += int(board[x][y]/5)
            board[x][y] -= int(board[x][y] / 5) * spreadCnt
    for x in range(n):
        for y in range(m):
            board[x][y] += addBoard[x][y]
    return
n, m, k = map(int,input().split())
board=[list(map(int,input().split()))for _ in range(n)]
purifierX = 0
for i in range(n):
    if board[i][0] == -1:
        purifierX = i
        break
for i in range(k):
    spread()
    purify(purifierX, 0, counterClockwise)
    purify(purifierX+1, 0, clockwise)
res = 0
for i in range(n):
    for j in range(m):
        if board[i][j] != -1: res += board[i][j]
print(res)