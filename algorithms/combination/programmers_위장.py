# https://programmers.co.kr/learn/courses/30/lessons/42578
# 1, 7 testcase 시간초과 => 직접 구하면 안되는 문젠가 싶었지만 같은 로직으로 자바 제출시 에누리없이 통과해버림..
from sys import*
input = lambda: stdin.readline().rstrip()

info = []
str_to_idx = {}
idx = 0
def solve(depth, pos):
    if depth == idx: return 1
    if len(info[depth]) == pos:
        return solve(depth+1, 0)
    # 선택 or 비선택
    return solve(depth+1, 0) + solve(depth, pos+1)
def solution(clothes):
    global idx
    for clothe, kind in clothes:
        if kind not in str_to_idx:
            str_to_idx[kind] = idx
            info.append([])
            idx += 1
        info[str_to_idx[kind]].append(clothe)
    return solve(0, 0) - 1
# print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))