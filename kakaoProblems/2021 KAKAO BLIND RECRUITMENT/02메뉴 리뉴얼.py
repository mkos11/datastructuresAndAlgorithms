# https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import*
class Node:
    def __init__(self, cnt=0, ans=[]):
        self.cnt = cnt
        self.ans = ans
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
    max_dic = {}
    for c in course:
        max_dic[c] = Node()
    ans = set()
    for t in total:
        cnt = 0
        for order in orders:
            if check(t, order): cnt += 1
        c = len(t)
        if max_dic[c].cnt < cnt:
            max_dic[c].cnt = cnt
            max_dic[c].ans = [t]
        elif max_dic[c].cnt == cnt:
            max_dic[c].ans.append(t)
    for k, v in max_dic.items():
        if v.cnt >= 2:
            for x in v.ans:
                ans.add(''.join(sorted(x)))
    return sorted(ans)
# print(solution(	["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))