# https://www.acmicpc.net/problem/17822
from sys import*
input=stdin.readline
def printf():
    for i in range(n):
        for j in range(m):
            print(board[i][j],end=' ')
        print()
    print()
# 클린코드에서 인자 많이쓰지 말랬는디
def rotate(x, d, k):
    global board
    for i in range(1, n+1):
        if i%x == 0:
            temp = []
            for j in range(m):
                if d==1:
                    temp.append(board[i-1][(j+k)%m])
                else:
                    temp.append(board[i-1][(j+(m-k))%m])
            for j in range(m):
                board[i-1][j] = temp[j]
def solve():
    global board
    fire = [[0]*m for _ in range(n)]
    total, cnt, fired = 0, 0, 0
    for x in range(n):
        for y in range(m):
            if board[x][y]:
                for dx, dy in [(0, 1), (1, 0)]:
                    # 다른 언어로 풀 시 %연산 다르게 해줘야함(음수 나머지 연산이 다름)
                    nx, ny = (x+dx), (y+dy)%m
                    if nx > n-1: continue
                    if board[nx][ny] == board[x][y]:
                        fire[nx][ny] = 1
                        fire[x][y] = 1
                        fired = 1
                cnt+=1
                total += board[x][y]
    if cnt: avg = total/cnt
    if not fired:
        for x in range(n):
            for y in range(m):
                if board[x][y]:
                    if board[x][y] > avg:
                        board[x][y] -= 1
                    elif board[x][y] < avg:
                        board[x][y] += 1
    else:
        for x in range(n):
            for y in range(m):
                if fire[x][y]: board[x][y] = 0
n, m, t = map(int, input().split())
board = [list(map(int, input().split()))for _ in range(n)]
for i in range(t):
    #x의 배수인 원판을 d방향(0시계, 1반시계)으로 k칸 회전
    x, d, k = map(int, input().split())
    rotate(x, d, k)
    # printf()
    solve()
    # printf()
res = 0
for i in range(n):
    res += sum(board[i])
print(res)