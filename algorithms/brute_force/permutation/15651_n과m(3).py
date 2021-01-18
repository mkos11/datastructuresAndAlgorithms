# n과m(3)
# https://www.acmicpc.net/problem/15651
from collections import*
def solve(cnt):
    if cnt == m:
        for i in range(m):
            print(q[i]+1, end=' ')
        print()
        return
    for i in range(n):
        q.append(i)
        solve(cnt+1)
        q.pop()
    return
n, m = map(int,input().split())
q=deque()
solve(0)