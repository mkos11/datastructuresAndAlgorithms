# https://www.acmicpc.net/problem/17142
from sys import*
from collections import*
input = stdin.readline
def cal():
    q=deque()
    visit = [[-1]*n for _ in range(n)]
    for x, y in picked_list:
        q.append((x, y))
        visit[x][y]=0
    spreadCnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visit[nx][ny]!=-1 or board[nx][ny]==1:continue
            if not board[nx][ny]:
                spreadCnt += 1
            visit[nx][ny] = visit[x][y]+1
            q.append((nx, ny))
            if spreadCnt == zeros: return visit[nx][ny]
    return INF
def solve(pos):
    global picked_list
    res = INF
    if pos == len(virus_list):
        if len(picked_list) == m:
            res = min(res, cal())
        return res
    picked_list.append(virus_list[pos])
    res = min(res, solve(pos+1))
    picked_list.pop()
    res = min(res, solve(pos+1))
    return res
INF=int(1e9)
n, m = map(int,input().split())
board=[list(map(int,input().split()))for _ in range(n)]
virus_list, picked_list = [], []
zeros = 0
for i in range(n):
    for j in range(n):
        if board[i][j]==2: virus_list.append((i, j))
        elif board[i][j]==0: zeros+=1
res = solve(0) if zeros else 0
print(res if res!=INF else -1)