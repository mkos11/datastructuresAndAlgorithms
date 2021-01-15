# https://www.acmicpc.net/problem/15686
from sys import*
input=stdin.readline
def cal():
    minSum = 0
    #집에서 무조건 치킨집 하나 골라야함
    for hx, hy in homeList:
        tempMin = INF
        for i in range(len(chickenStores)):
            if checked[i]:
                cx, cy = chickenStores[i]
                tempMin = min(tempMin, abs(hx-cx) + abs(hy-cy))
        minSum += tempMin
    return minSum
def solve(pos, cnt):
    res = INF
    if cnt > m: return res
    if pos == len(chickenStores):
        if cnt == m:
            res = min(res, cal())
        return res
    checked[pos] = 1
    res = min(res, solve(pos+1, cnt+1))
    checked[pos] = 0
    res = min(res, solve(pos+1, cnt))
    return res
INF = int(1e9)
n, m = map(int,input().split())
board=[list(map(int,input().split()))for _ in range(n)]
homeList = []
chickenStores = []
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            homeList.append((i, j))
        elif board[i][j]==2:
            chickenStores.append((i, j))
checked = [0]*len(chickenStores)
print(solve(0, 0))