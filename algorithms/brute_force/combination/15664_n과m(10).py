# n과m(10)
# https://www.acmicpc.net/problem/15664
def solve(pos, cnt):
    if cnt == m:
        for i in range(m):
            print(stack[i], end=' ')
        print()
        return
    prev = -1
    for i in range(pos, n):
        if not visit[i] and prev != arr[i]:
            visit[i] = 1
            stack.append(arr[i])
            solve(i, cnt+1)
            stack.pop()
            visit[i] = 0
            prev = arr[i]
n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visit=[0]*n
stack = []
solve(0, 0)

'''
# 이것도 사전 없이 처리 가능할듯
from collections import*
def solve(pos, cnt):
    if cnt == m:
        temp = []
        for i in range(m):
            temp.append(stack[i])
        temp = tuple(temp)
        if temp not in dic:
            dic[temp] = 1
        return
    for i in range(pos, n):
        if not visit[i]:
            visit[i] = 1
            stack.append(arr[i])
            solve(i, cnt+1)
            visit[i] = 0
            stack.pop()

n, m = map(int,input().split())
visit=[0]*n
arr = list(map(int,input().split()))
arr.sort()
stack = []
dic = {}
solve(0, 0)
for key, value in dic.items():
    for x in key:
        print(x, end=' ')
    print()
'''