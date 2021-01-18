# n과m(7)
# https://www.acmicpc.net/problem/15656
from collections import*
def solve(cnt):
    if cnt == m:
        for i in range(m):
            print(q[i], end=' ')
        print()
        return
    for i in range(n):
        q.append(arr[i])
        solve(cnt+1)
        q.pop()
    return
n, m = map(int,input().split())
q=deque()
arr = list(map(int,input().split()))
arr.sort()
solve(0)