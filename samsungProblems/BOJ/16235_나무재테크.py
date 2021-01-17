# https://www.acmicpc.net/problem/16235
# pypy3 제출
from sys import*
from collections import*
input=stdin.readline
dd=[(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
def solve():
    global trees, nutritions
    #봄, 여름
    for i in range(n):
        for j in range(n):
            died = 0
            treeLen = len(trees[i][j])
            for t in range(treeLen):
                age = trees[i][j].popleft()
                if age <= nutritions[i][j]:
                    nutritions[i][j] -= age
                    trees[i][j].append(age+1)
                else:
                    died += int(age/2)
            nutritions[i][j] += died
    #가을, 겨울
    for i in range(n):
        for j in range(n):
            treeLen = len(trees[i][j])
            for t in range(treeLen):
                age = trees[i][j][t]
                if age % 5 == 0:
                    for dx, dy in dd:
                        nx, ny = i+dx, j+dy
                        if nx<0 or ny<0 or nx>n-1 or ny>n-1:continue
                        trees[nx][ny].appendleft(1)
            nutritions[i][j] += addNutritions[i][j]

n, m, k = map(int,input().split())
addNutritions = [list(map(int,input().split()))for _ in range(n)]
nutritions = [[5]*n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
for i in range(m):
    x, y, z = map(int,input().split())
    trees[x-1][y-1].append(z)
for i in range(k):
    solve()
res = 0
for i in range(n):
    for j in range(n):
        res += len(trees[i][j])
print(res)