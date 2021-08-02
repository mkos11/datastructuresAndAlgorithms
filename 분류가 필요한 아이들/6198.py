# https://www.acmicpc.net/problem/6198
from sys import*
input = stdin.readline

class Node:
    def __init__(self, height, idx):
        self.height = height
        self.idx = idx
    def __str__(self):
        return f"{self.height} {self.idx}"

stack = []
res = 0
n = int(input())
# 마지막에 엄청 큰 수 놔서 처리 안된것들 처리
for i in range(n + 1):
    if i == n: h = int(1e18)
    else: h = int(input())
    while stack:
        if stack[-1].height <= h:
            node = stack.pop()
            res += (i - node.idx - 1)
        else: break
    stack.append(Node(h, i))
print(res)