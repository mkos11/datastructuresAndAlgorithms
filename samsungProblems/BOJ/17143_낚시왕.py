# https://www.acmicpc.net/problem/17143
# pypy3 제출
# 큐에 상어 정보 넣고 dic로 체크하면서 상어 정보 채워넣는 식으로 짜면 될듯?
# 잡는건?? 2차원 board 하나 만들어야 할듯
from sys import*
from collections import*
input = stdin.readline
def changeDirection(d):
    if d==U: return D
    if d==R: return L
    if d==L: return R
    if d==D: return U
U, R, D, L = (-1, 0), (0, 1), (1, 0), (0, -1)
directions = [U, D, R, L]
n, m, k = map(int, input().split())
sharks = {}
q = deque()
fishingList = []
fisher = 1
for i in range(k):
    x, y, speed, d, size = map(int,input().split())
    q.append((x, y, speed, directions[d-1], size))
    if y==fisher: fishingList.append((x, y, size))

res = 0
for i in range(m):
    died = (-1, -1)
    if fishingList:
        fishingList.sort(key = lambda x:x[0])
        x, y, size = fishingList[0]
        died = (x, y)
        res += size
    sharks = {}
    fishingList = []
    fisher += 1
    if not q: break
    while q:
        x, y, speed, d, size = q.popleft()
        if died == (x, y): continue
        dx, dy = d
        for _ in range(speed):
            x, y = x+dx, y+dy
            if x<1 or y<1 or x>n or y>m:
                d = changeDirection(d)
                dx, dy = d
                x, y = x+(2*dx), y+(2*dy)
        if (x, y) not in sharks:
            sharks[(x, y)] = (speed, d, size)
        elif sharks[(x, y)][2] < size:
            sharks[(x, y)] = (speed, d, size)
    for (x, y), (speed, d, size) in sharks.items():
        q.append((x, y, speed, d, size))
        if y==fisher: fishingList.append((x, y, size))
print(res)