# https://www.acmicpc.net/problem/16236
from heapq import*
from sys import*
input=stdin.readline
n=int(input())
ocean = [list(map(int,input().split()))for _ in range(n)]
for i in range(n):
    for j in range(n):
        if ocean[i][j] == 9:
            x, y = i, j
            ocean[x][y] = 0
            break
size, eated = 2, 0
res = 0
pq = []
heappush(pq,(0, x, y))
visit = [[0]*n for _ in range(n)]
while pq:
    d, x, y = heappop(pq)
    visit[x][y] = 1
    if 0 < ocean[x][y] < size:
        ocean[x][y] = 0
        eated += 1
        if size == eated:
            eated = 0
            size += 1
        pq = []
        res += d
        d = 0
        heappush(pq, (d, x, y))
        visit = [[0]*n for _ in range(n)]
    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visit[nx][ny] or ocean[nx][ny] > size: continue
        heappush(pq, (d+1, nx, ny))
        visit[nx][ny] = 1
print(res)
'''
#이렇게도 되는데 pq 하나로 더 간단히 가능
from heapq import*
from collections import*
n=int(input())
ocean = [list(map(int,input().split()))for _ in range(n)]
for i in range(n):
    for j in range(n):
        if ocean[i][j] == 9:
            x, y = i, j
            ocean[x][y] = 0
            break
size, eated = 2, 0
q=deque()
q.append((x, y, 0))
res = 0
visited = [[0]*n for _ in range(n)]
while q:
    lq = len(q)
    pq = []
    for i in range(lq):
        x, y, t = q.popleft()
        visited[x][y] = 1
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visited[nx][ny] or ocean[nx][ny] > size: continue
            if 0 < ocean[nx][ny] < size:
                heappush(pq, (nx, ny, t+1))
                continue
            q.append((nx, ny, t+1))
            #와 이거때문에 시간초과뜸!!!!!!!!! 주의
            visited[nx][ny] = 1
    if pq:
        x, y, t = heappop(pq)
        ocean[x][y] = 0
        eated += 1
        if eated >= size:
            size += 1
            eated = 0
        res += t
        visited = [[0]*n for _ in range(n)]
        q=deque()
        q.append((x, y, 0))
print(res)
'''