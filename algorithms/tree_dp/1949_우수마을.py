# https://www.acmicpc.net/problem/1949
# 트리 dp

from sys import*
setrecursionlimit(10**6)
input = stdin.readline

def make_tree(u):
    visit[u] = True
    for v in adj[u]:
        if visit[v]: continue
        child[u].append(v)
        make_tree(v)
def solve(picked, u):
    if mem[picked][u] != -1: return mem[picked][u]
    mem[picked][u] = 0
    for v in child[u]:
        if picked:
            mem[picked][u] += solve(0, v)
        else:
            # 적어도 하나 인접하는 조건은 신경 안써줘도 어차피 최댓값 찾는 부분에서 알아서 만족됨
            mem[picked][u] += max(solve(1, v) + people[v], solve(0, v))
    return mem[picked][u]
n = int(input())
people = list(map(int, input().split()))
adj = [[]for _ in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    adj[u].append(v)
    adj[v].append(u)
child = [[]for _ in range(n)]
visit = [False] * n
make_tree(0)
mem = [[-1] * n for _ in range(2)]
print(max(solve(0, 0), solve(1, 0) + people[0]))