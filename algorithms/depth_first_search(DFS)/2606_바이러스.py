# https://www.acmicpc.net/problem/2606
from sys import*
input = stdin.readline
setrecursionlimit(10**6)
def dfs(u):
    global virus
    virus += 1
    visit[u] = 1
    for v in adj[u]:
        if not visit[v]:
            dfs(v)
computerCnt = int(input())
adj = [[]for _ in range(computerCnt)]
for i in range(int(input())):
    x, y = map(int,input().split())
    x-=1; y-=1
    # 이 문제는 제한이 적어서 그냥 추가 했는데 중복 많아서 set() 같은거로 중복처리 해줘야 하는 문제도 있음
    adj[x].append(y)
    adj[y].append(x)
visit = [0]*computerCnt
virus = -1  #자기 자신 빼고 세어야 해서 미리 빼줌
dfs(0)
print(virus)
