# https://www.acmicpc.net/problem/2533
# 트리dp
from sys import *
setrecursionlimit(10**6)
input = lambda: stdin.readline().rstrip()
def make_tree(u):
    visit[u] = True
    for v in adj[u]:
        if visit[v]: continue
        child[u].append(v)
        make_tree(v)
def solve(prev, u):
    if mem[prev][u] != -1: return mem[prev][u]
    mem[prev][u] = 0
    for v in child[u]:
        # 전에 칠했으면 다음거 칠하거나 안칠하거나
        if prev == 1: mem[prev][u] += min(solve(1, v) + 1, solve(0, v))
        # 안칠했으면 무조건 칠함
        else: mem[prev][u] += solve(1, v) + 1
    return mem[prev][u]
n = int(input())
adj = [[]for _ in range(n)]
# 트리 정의상 어느 곳이든 루트가 될 수 있음, 어떤게 부모가 될지 모르므로 양방향으로 처리하고 visit으로 걸러줘야함
for i in range(n-1):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    adj[u].append(v)
    adj[v].append(u)
visit = [False] * n
mem = [[-1]*n for _ in range(2)]
child = [[]for _ in range(n)]
make_tree(0)
print(min(solve(1, 0)+1, solve(0, 0)))
# print(mem)