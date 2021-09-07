# https://programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    return min(len(set(nums)), len(nums)//2)
print(solution(	[3, 1, 2, 3]))