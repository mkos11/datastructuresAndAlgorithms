# n과m(4)
# https://www.acmicpc.net/problem/15652
def solve(pos, cnt):
    if cnt == m:
        for i in range(m):
            print(stack[i]+1, end=' ')
        print()
        return
    for i in range(pos, n):
        stack.append(i)
        solve(i, cnt+1)
        stack.pop()
    return
n, m = map(int,input().split())
stack = []
solve(0, 0)
