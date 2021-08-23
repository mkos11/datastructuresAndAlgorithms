# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    zero_cnt = 0
    same_cnt = 0
    for lotto in lottos:
        if lotto == 0: zero_cnt += 1
        elif lotto in win_nums: same_cnt += 1
    return [rank[same_cnt+zero_cnt], rank[same_cnt]]
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))