# n과m(8)
# https://www.acmicpc.net/problem/15657
def solve(pos, cnt):
    if cnt == m:
        for i in range(m):
            print(stack[i], end=' ')
        print()
        return
    for i in range(pos, n):
        stack.append(arr[i])
        solve(i, cnt+1)
        stack.pop()
    return
n, m = map(int,input().split())
stack = []
arr = list(map(int,input().split()))
arr.sort()
solve(0, 0)