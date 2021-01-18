# n과m(11)
# https://www.acmicpc.net/problem/15665

from collections import*
def solve(cnt):
    if cnt == m:
        for i in range(m):
            print(q[i], end=' ')
        print()
        return
    prev = -1
    for i in range(n):
        if prev != arr[i]:
            q.append(arr[i])
            solve(cnt+1)
            q.pop()
            prev = arr[i]
n, m = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
q=deque()
solve(0)

'''
from collections import*
def solve(cnt):
    if cnt == m:
        temp=[]
        for i in range(m):
            temp.append(q[i])
        temp = tuple(temp)
        if temp not in dic:
            dic[temp] = 1
        return
    for i in range(n):
        q.append(arr[i])
        solve(cnt+1)
        q.pop()

n, m = map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
dic = {}
q=deque()
solve(0)
for key, value in dic.items():
    for x in key:
        print(x, end=' ')
    print()
'''