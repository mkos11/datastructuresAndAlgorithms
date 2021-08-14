# https://programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    poket = set(nums)
    return min(len(poket), len(nums)//2)
