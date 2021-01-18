# n과m(5)
# https://www.acmicpc.net/problem/15654
def solve(cnt):
    if cnt == m:
        for i in range(m):
            print(stack[i], end=' ')
        print()
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            stack.append(arr[i])
            solve(cnt+1)
            visit[i] = 0
            stack.pop()
    return
n, m = map(int,input().split())
stack = []
visit=[0]*n
arr = list(map(int,input().split()))
arr.sort()
solve(0)