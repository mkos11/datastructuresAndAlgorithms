# https://www.acmicpc.net/problem/15657
from collections import*
def solve(pos, cnt):
    if cnt == m:
        for i in range(m):
            print(q[i], end=' ')
        print()
        return
    for i in range(pos, n):
        q.append(arr[i])
        solve(i, cnt+1)
        q.pop()
    return
n, m = map(int,input().split())
q=deque()
arr = list(map(int,input().split()))
arr.sort()
solve(0, 0)