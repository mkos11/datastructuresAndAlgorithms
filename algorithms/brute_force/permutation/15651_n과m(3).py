# n과m(3)
# https://www.acmicpc.net/problem/15651
def solve(cnt):
    if cnt == m:
        for i in range(m):
            print(stack[i]+1, end=' ')
        print()
        return
    for i in range(n):
        stack.append(i)
        solve(cnt+1)
        stack.pop()
    return
n, m = map(int,input().split())
stack = []
solve(0)