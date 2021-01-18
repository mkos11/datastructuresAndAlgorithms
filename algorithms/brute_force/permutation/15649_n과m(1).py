# n과m(1)
# https://www.acmicpc.net/problem/15649
'''
# 라이브러리 사용
from itertools import*

n, m = map(int,input().split())
for p in permutations(range(1, n+1), m):
    for x in p:
        print(x, end= ' ')
    print()
'''
from collections import*
def solve(cnt):
    global q
    if cnt == m:
        for i in range(m):
            print(q[i]+1, end=' ')
        print()
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            q.append(i)
            solve(cnt+1)
            q.pop()
            visit[i] = 0
n ,m = map(int,input().split())
visit = [0]*n
q=deque()
solve(0)