from sys import*

#URDL
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def solve():
    n, m = map(int,input().split())
    x, y, d = map(int,input().split())
    board=[list(map(int,input().split()))for _ in range(n)]
    cleanCnt = 0

    while True:
        if not board[x][y]:
            board[x][y] = 2
            cleanCnt += 1
        clean = False
        for i in range(4):
            d = (d+3)%4
            dx, dy = dd[d]
            nx, ny = x+dx, y+dy
            if board[nx][ny]==0:
                x, y = nx, ny
                clean = True
                break
        if not clean:
            x, y = x-dx, y-dy
            if board[x][y] == 2: continue
            return cleanCnt

print(solve())