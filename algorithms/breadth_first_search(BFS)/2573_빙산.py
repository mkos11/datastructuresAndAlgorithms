# https://www.acmicpc.net/problem/2573

# dfs 시간초과 뭐냐고.. bfs()로 풀고 pypy3제출이 정신건강에 이롭..
# pypy3 제출
from sys import*
from collections import*
input = stdin.readline
dd = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(x, y):
    q=deque()
    q.append((x, y))
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dd:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>m-1 or visit[nx][ny]: continue
            if board[nx][ny] <= 0: board[x][y] -= 1
            else:
                visit[nx][ny]=1
                q.append((nx, ny))

n, m = map(int,input().split())
board = [list(map(int,input().split()))for _ in range(n)]
time = 0
while 1:
    lump = 0
    visit = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visit[i][j] and board[i][j]>0:
                lump += 1
                bfs(i, j)
    if lump >= 2:
        print(time)
        break
    elif lump == 0:
        print(0)
        break
    time += 1