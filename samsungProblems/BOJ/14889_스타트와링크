# https://www.acmicpc.net/problem/14889
def cal():
    lTeam, rTeam = 0, 0
    for i in range(n):
        for j in range(i+1, n):
            if visit[i] and visit[j]:
                lTeam += score[i][j] + score[j][i]
            elif not visit[i] and not visit[j]:
                rTeam += score[i][j] + score[j][i]
    return abs(lTeam - rTeam)
def solve(pos, cnt):
    global visit
    res = INF
    if cnt > n//2: return res
    if pos == n:
        if cnt == n//2:
            res = min(res, cal())
        return res
    visit[pos] = 1
    res = min(res, solve(pos+1, cnt+1))
    visit[pos] = 0
    res = min(res, solve(pos+1, cnt))
    return res
INF = 1e9
n=int(input())
score=[list(map(int,input().split())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
print(solve(0, 0))