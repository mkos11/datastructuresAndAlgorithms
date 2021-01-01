# https://www.acmicpc.net/problem/1874
from sys import*
input=stdin.readline

n = int(input())
cur = 1
stack = []
ans = []
res = []
for i in range(n):
    ans.append(int(input()))

pos = 0
while pos < n and cur <= n:
    if stack and stack[-1] == ans[pos]:
        pos += 1
        stack.pop()
        res.append('-')
    else:
        stack.append(cur)
        cur += 1
        res.append('+')
while stack:
    if stack[-1] == ans[pos]:
        pos += 1
        stack.pop()
        res.append('-')
    else:
        break
if stack: print('NO')
else:
    for x in res: print(x)