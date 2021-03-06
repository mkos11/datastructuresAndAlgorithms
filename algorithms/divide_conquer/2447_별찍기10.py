def solve(x, y, size):
    if size == 1:
        board[x][y]='*'
        return
    nextSize = size//3
    for i in range(3):
        for j in range(3):
            # 가운데 부분 넘김
            if i == 1 and j == 1: continue
            solve(x+i*nextSize, y+j*nextSize, nextSize)
n = int(input())
board = [[' ']*n for _ in range(n)]
solve(0, 0, n)
for i in range(n):
    print(''.join(board[i]))
