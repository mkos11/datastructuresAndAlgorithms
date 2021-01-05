# https://www.acmicpc.net/problem/12100
U, R, D, L = 0, 1, 2, 3
def cal(sx, sy, dx, dy):
    global board, MAX
    x, y = sx, sy
    stack = []
    idx = 0
    for i in range(n):
        if board[x][y]:
            if len(stack) <= idx:
                stack.append(board[x][y])
            else:
                if stack[idx] == board[x][y]:
                    stack[idx] *= 2
                    MAX = max(MAX, stack[idx])
                else:
                    stack.append(board[x][y])
                idx += 1
            board[x][y]=0
        x, y = x+dx, y+dy
    for i in range(len(stack)):
        board[sx][sy] = stack[i]
        sx, sy = sx+dx, sy+dy

def move(d):
    #옮기는 방향마다 살펴보는 시작점, 이동 방향 다름
    for i in range(n):
        if d == U: cal(0, i, 1, 0)
        if d == R: cal(i, n-1, 0, -1)
        if d == D: cal(n-1, i, -1, 0)
        if d == L: cal(i, 0, 0, 1)

def solve(depth):
    global MAX, board
    #0부터 시작하니까 5됐을때 끝내줘야함(최대 5번 이동 가능)
    if depth == 5: return
    temp = [x[:] for x in board]
    for i in range(4):
        move(i)
        solve(depth+1)
        board = [x[:] for x in temp]
n=int(input())
board=[list(map(int,input().split()))for _ in range(n)]
MAX = -1
for i in range(n):
    MAX = max(MAX, max(board[i]))

solve(0)
print(MAX)