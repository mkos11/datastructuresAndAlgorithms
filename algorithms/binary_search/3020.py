# https://www.acmicpc.net/problem/3020
# 이진탐색
from sys import*
input = stdin.readline

class Node:
    def __init__(self, val):
        self.min_val = val
        self.cnt = 1
def lower_bound(height, rock):
    l = 0
    r = len(rock) - 1
    while l <= r:
        mid = (l + r) // 2
        if rock[mid] >= height:
            r = mid - 1
        else:
            l = mid + 1
    return l

def solve(height, rock):
    return len(rock) - lower_bound(height, rock)

n, h = map(int, input().split())
up = []
down = []
for i in range(n):
    if i % 2 == 0:
        up.append(int(input()))
    else:
        down.append(int(input()))
up.sort()
down.sort()
INF = int(1e9)
res = Node(INF)
for i in range(h):
    val = solve(h-i, up) + solve(i+1, down)
    if res.min_val > val: res = Node(val)
    elif res.min_val == val: res.cnt += 1
print(res.min_val, res.cnt)