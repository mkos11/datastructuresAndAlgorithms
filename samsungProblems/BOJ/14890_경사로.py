# https://www.acmicpc.net/problem/14890
def detect(x, y, dx, dy):
    canBuild = 1
    for i in range(n-1):
        nx, ny = x+dx, y+dy
        if abs(board[nx][ny] - board[x][y]) > 1: return 0
        if board[nx][ny] > board[x][y]:
            if canBuild >= L:
                canBuild = 1
            else:
                return 0
        elif board[nx][ny] < board[x][y]:
            if canBuild < 0: return 0
            else:
                canBuild = -L+1
        else:
            canBuild += 1
        x, y = nx, ny
    if canBuild >= 0: return 1
    return 0
n, L = map(int,input().split())
board=[list(map(int,input().split()))for _ in range(n)]
res = 0
for i in range(n):
    if detect(0, i, 1, 0): res += 1
    if detect(i, 0, 0, 1): res += 1
print(res)