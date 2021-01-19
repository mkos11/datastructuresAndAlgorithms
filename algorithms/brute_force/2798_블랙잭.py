# https://www.acmicpc.net/problem/2798
def solve(pos, cnt, total):
    res = 0
    #cnt도 가지치기 해줘야함
    if total > m or cnt > 3: return 0
    if pos == n:
        if cnt == 3:
            res = max(res, total)
        return res
    res = max(res, solve(pos+1, cnt+1, total+cards[pos]))
    res = max(res, solve(pos+1, cnt, total))
    return res
n, m = map(int,input().split())
cards = list(map(int,input().split()))
print(solve(0, 0, 0))