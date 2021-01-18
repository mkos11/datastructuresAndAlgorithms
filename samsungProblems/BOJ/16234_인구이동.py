# https://www.acmicpc.net/problem/16234
# pypy3 제출
from sys import*
from collections import*
input=stdin.readline

def merge(x, y):
    global borad, visited
    visited[x][y]=1
    q = deque()
    q.append((x, y))
    people = board[x][y]
    unionList = []
    unionList.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in dd:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visited[nx][ny]: continue
            if L <= abs(board[nx][ny]-board[x][y]) <= R:
                unionList.append((nx, ny))
                q.append((nx, ny))
                people += board[nx][ny]
                visited[nx][ny] = 1
    if len(unionList) == 1: return 0
    for x, y in unionList:
        board[x][y] = int(people/len(unionList))
    return 1

n, L, R = map(int,input().split())
board = [list(map(int,input().split()))for _ in range(n)]
dd=[(0,1),(0,-1),(1,0),(-1,0)]
for m in range(2001):
    isMove = False
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and merge(i, j):
                isMove = True
    if not isMove:
        print(m)
        break