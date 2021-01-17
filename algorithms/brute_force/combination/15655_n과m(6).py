# https://www.acmicpc.net/problem/15655
from collections import*
def solve(pos, cnt):
    if cnt == m:
        for i in range(m):
            print(q[i], end=' ')
        print()
        return
    for i in range(pos, n):
        if not visit[i]:
            visit[i] = 1
            q.append(arr[i])
            solve(i, cnt+1)
            visit[i] = 0
            q.pop()
    return
n, m = map(int,input().split())
q=deque()
visit=[0]*n
arr = list(map(int,input().split()))
arr.sort()
solve(0, 0)