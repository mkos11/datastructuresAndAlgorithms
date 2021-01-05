# https://www.acmicpc.net/problem/3190
from collections import*
dd = [(0, 1), (1, 0), (0, -1), (-1, 0)] #RDLU
def solve():
    n = int(input())
    board=[[0]*n for _ in range(n)]
    turningPoint = deque()
    for i in range(int(input())):
        x, y = map(int, input().split())
        board[x-1][y-1] = 1

    for i in range(int(input())):
        t, dInfo = map(str, input().split())
        turningPoint.append((int(t), dInfo))
    tail=deque()
    tail.append((0, 0))
    x, y, d, time = 0, 0, 0, 0
    while 1:
        time += 1
        dx, dy = dd[d]
        x, y = x+dx, y+dy
        if x<0 or y<0 or x>n-1 or y>n-1 or board[x][y]==2: return time
        if board[x][y]==0:
            tx, ty = tail.popleft()
            board[tx][ty] = 0
        if turningPoint and turningPoint[0][0] <= time:
            t, dInfo = turningPoint.popleft()
            if dInfo=='L': d=(d+3)%4
            elif dInfo=='D': d=(d+1)%4
        tail.append((x, y))
        board[x][y]=2
print(solve())