# https://www.acmicpc.net/problem/1725
from sys import*
input=stdin.readline

TOP = -1
heights = []
n=int(input())
stack = []
res = 0

for i in range(n+1):
    if i<n: heights.append(int(input()))
    else: heights.append(0)
    while stack and (heights[stack[TOP]] >= heights[i]):
        cur = stack.pop()
        if not stack: res = max(res, heights[cur] * i)
        else: res = max(res, heights[cur] * (i - stack[TOP] - 1))
    stack.append(i)
print(res)