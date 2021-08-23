# https://programmers.co.kr/learn/courses/30/lessons/12977
# 제한이 작아서 그냥 소수 막 구했는데 이거 그 무슨 체로 빠르게 가능 리뷰때 고치기
def isPrime(num):
    for i in range(2, num):
        if num % i == 0: return False
    return True
def solve(pos, nums, cnt, sum):
    res = 0
    if cnt > 3: return 0
    if pos == len(nums):
        if cnt == 3:
            res += isPrime(sum)
        return res
    res += solve(pos+1, nums, cnt+1, sum+nums[pos])
    res += solve(pos+1, nums, cnt, sum)
    return res
def solution(nums):
    return solve(0, nums, 0, 0)

print(solution(	[1, 2, 7, 6, 4]))