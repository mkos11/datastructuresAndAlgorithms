from sys import*
input = stdin.readline
INF = int(1e9)
cnt = {-1: 0, 0: 0, 1: 0}
def solve(x, y, size):
    if size == 1:
        cnt[board[x][y]] += 1
        return board[x][y]
    nextSize = size//3
    prev = -INF
    flag = True
    for i in range(3):
        for j in range(3):
            curr = solve(x+i*nextSize, y+j*nextSize, nextSize)
            if prev==-INF or prev == curr:
                prev = curr
            else:
                # 다름
                flag = False
    if not flag or prev==INF: return INF
    cnt[prev] -= 8
    return prev
n = int(input())
board = [list(map(int, input().split()))for _ in range(n)]
solve(0, 0, n)
for k, v in cnt.items():
    print(v)
