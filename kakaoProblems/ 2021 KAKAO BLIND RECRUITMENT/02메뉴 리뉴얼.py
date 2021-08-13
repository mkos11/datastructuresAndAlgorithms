# https://programmers.co.kr/learn/courses/30/lessons/72411
# 시간초과 날거 같은데????????? 한번 일단 풀어보기 난다 => 담부터 완전 잘 보고 풀기, 안난다 => 담부터 낮은 단계는 일단 풀기
from itertools import*
def check(total, order):
    for t in total:
        if t not in order: return False
    return True
def solution(orders, course):
    total = set()
    for order in orders:
        for c in course:
            for x in combinations(order, c):
                total.add(x)
    ans = set()
    for t in total:
        cnt = 0
        for order in orders:
            if check(t, order): cnt += 1
            if cnt >= 2:
                ans.add(t)
                break
    print(ans)

print(solution(	["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))