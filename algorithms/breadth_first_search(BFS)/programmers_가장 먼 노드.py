# https://programmers.co.kr/learn/courses/30/lessons/49189
from collections import*
def bfs(adj, visit):
    q = deque()
    q.append(0)
    visit[0] = 0
    max_len = 0
    cnt = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if visit[v] == -1:
                visit[v] = visit[u] + 1
                q.append(v)
                if visit[v] == max_len: cnt += 1
                elif visit[v] > max_len:
                    max_len = visit[v]
                    cnt = 1
    return cnt
def solution(n, edge):
    adj = [[] for _ in range(n)]
    visit = [-1]*n
    for u, v in edge:
        u -= 1; v -= 1
        adj[u].append(v)
        adj[v].append(u)
    return bfs(adj, visit)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))