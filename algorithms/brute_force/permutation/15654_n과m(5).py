# n과m(5)
# https://www.acmicpc.net/problem/15654
from collections import*
def solve(cnt):
    if cnt == m:
        for i in range(m):
            print(q[i], end=' ')
        print()
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            q.append(arr[i])
            solve(cnt+1)
            visit[i] = 0
            q.pop()
    return
n, m = map(int,input().split())
q=deque()
visit=[0]*n
arr = list(map(int,input().split()))
arr.sort()
solve(0)