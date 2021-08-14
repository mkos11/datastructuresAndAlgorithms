# https://programmers.co.kr/learn/courses/30/lessons/43238
def cal(times, m):
    res = 0
    for time in times:
        res += (m // time)
    return res
def solution(n, times):
    l, r = 0, int(1e18)
    while l <= r:
        m = (l + r) // 2
        if n <= cal(times, m):
            r = m - 1
        else:
            l = m + 1
    return l
print(solution(	6, [7, 10]))