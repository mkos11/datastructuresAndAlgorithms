from sys import*
setrecursionlimit(10**6)
input = stdin.readline
def init():
    global visit, maxLen, maxNode
    visit = [False] * n
    maxLen = 0
    maxNode = 0
def solve(u, length):
    global visit, maxLen, maxNode
    visit[u] = True
    if maxLen < length:
        maxNode = u
        maxLen = length
    for v, k in adj[u]:
        if not visit[v]:
            solve(v, length + k)
n = int(input())
adj = [[]*n for _ in range(n)]
for i in range(n-1):
    u, v, k = map(int,input().split())
    u -= 1
    v -= 1
    adj[u].append((v, k))
    adj[v].append((u, k))
init()
solve(0, 0)                #루트에서 가장 긴 리프노드
longLeaf = maxNode
init()
solve(longLeaf, 0)         #리프에서 가장 긴 리프노드
print(maxLen)

