from sys import*
from collections import*
input=stdin.readline
def solve():
    q=deque()
    q.append(u)
    visit=[-1]*n
    visit[u]=0
    while q:
        cur = q.popleft()
        if cur == v: return visit[cur]
        for nxt in adj[cur]:
            if visit[nxt]==-1:
                q.append(nxt)
                visit[nxt] = visit[cur]+1
    return -1

n=int(input())
adj=[[]*n for _ in range(n)]
u, v = map(int,input().split())
u-=1; v-=1
for i in range(int(input())):
    x, y = map(int,input().split())
    adj[x-1].append(y-1)
    adj[y-1].append(x-1)
print(solve())