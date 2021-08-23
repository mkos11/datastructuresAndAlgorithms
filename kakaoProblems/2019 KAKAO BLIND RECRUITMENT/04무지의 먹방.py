# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3#
from heapq import*
from sys import*
input = lambda: stdin.readline().rstrip()
class Node:
    def __init__(self, food_time, idx):
        self.food_time = food_time
        self.idx = idx
    # less than, 반환값이 True면 self 값이 더 작다는 뜻, 따라서 여러개도 비교 가능
    def __lt__(self, other):
        return self.food_time < other.food_time
    def __str__(self):
        return f'\nfood_time: {self.food_time} idx: {self.idx}'
def solution(food_times, k):
    info = []
    for i, food_time in enumerate(food_times):
        heappush(info, Node(food_time, i+1))
    eated = 0
    while info and len(info) <= k:
        k -= len(info)
        eated += 1
        while info:
            if eated >= info[0].food_time:
                heappop(info)
            else:
                break
    res = []
    while info:
        res.append(heappop(info))
    return sorted(res, key = lambda x: x.idx)[k].idx if res else -1
print(solution([3, 1, 2], 5))