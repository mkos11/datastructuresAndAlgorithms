# https://www.acmicpc.net/problem/15652
from collections import*

def solve(pos, cnt):
    if cnt == m:
        for i in range(m):
            print(q[i]+1, end=' ')
        print()
        return
    for i in range(pos, n):
        q.append(i)
        solve(i, cnt+1)
        q.pop()
    return
n, m = map(int,input().split())
q=deque()
solve(0, 0)
