def solve(pos, total):
    res = 0
    if pos == n:
        if total == s:
            return 1
        return 0
    res += solve(pos+1, total+arr[pos])
    res += solve(pos+1, total)
    return res
n, s = map(int, input().split())
arr = list(map(int,input().split()))
# 초기 total = 0 으로 넣어줘서, s = 0 일 때 하나도 선택되지 않은 경우 +1이됨, 그거 제거해줘야함
res = solve(0, 0)
print(res if s!=0 else res-1)