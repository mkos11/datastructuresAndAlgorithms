# n과m(7)
# https://www.acmicpc.net/problem/15656
def solve(cnt):
    if cnt == m:
        for i in range(m):
            print(stack[i], end=' ')
        print()
        return
    for i in range(n):
        stack.append(arr[i])
        solve(cnt+1)
        stack.pop()
    return
n, m = map(int,input().split())
stack = []
arr = list(map(int,input().split()))
arr.sort()
solve(0)