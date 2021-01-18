# n과m(12)
# https://www.acmicpc.net/problem/15666

from collections import*
def solve(pos, cnt):
    if cnt == m:
        for i in range(m):
            print(q[i], end=' ')
        print()
        return
    prev = -1
    for i in range(pos, n):
        if prev != arr[i]:
            q.append(arr[i])
            solve(i, cnt+1)
            q.pop()
            prev = arr[i]
n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
q=deque()
solve(0, 0)
'''
# 이것도 사전 없이 처리 가능할듯
from collections import*
def solve(pos, cnt):
    if cnt == m:
        temp = []
        for i in range(m):
            temp.append(q[i])
        temp = tuple(temp)
        if temp not in dic:
            dic[temp] = 1
        return
    for i in range(pos, n):
        q.append(arr[i])
        solve(i, cnt+1)
        q.pop()

n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
q=deque()
dic = {}
solve(0, 0)
for key, value in dic.items():
    for x in key:
        print(x, end=' ')
    print()
'''