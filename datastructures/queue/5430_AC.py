# https://www.acmicpc.net/problem/5430
from sys import*
from collections import*
input = lambda: stdin.readline().rstrip()

def solve():
    reverse = False
    p = input()
    n = int(input())
    arr = input()[1:-1]
    q = deque(list(map(int, arr.split(',')))) if n != 0 else deque(arr)
    for x in p:
        if x == 'R': reverse = not reverse
        elif x == 'D':
            if len(q) == 0: return 'error'
            if reverse:
                q.pop()
            else:
                q.popleft()
    res = []
    while q:
        if reverse: res.append(str(q.pop()))
        else: res.append(str(q.popleft()))
    return '[' + ','.join(res) + ']'
for tc in range(int(input())):
    print(solve())