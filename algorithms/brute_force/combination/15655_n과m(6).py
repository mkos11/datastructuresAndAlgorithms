# n과m(6)
# https://www.acmicpc.net/problem/15655
def solve(pos, cnt):
    if cnt == m:
        for i in range(m):
            print(stack[i], end=' ')
        print()
        return
    for i in range(pos, n):
        if not visit[i]:
            visit[i] = 1
            stack.append(arr[i])
            solve(i, cnt+1)
            visit[i] = 0
            stack.pop()
    return
n, m = map(int,input().split())
stack = []
visit=[0]*n
arr = list(map(int,input().split()))
arr.sort()
solve(0, 0)