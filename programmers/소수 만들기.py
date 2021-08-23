# https://programmers.co.kr/learn/courses/30/lessons/12977
# review => 에라토스테네스의 체 써서 빠르게

# def isPrime(num):
#     for i in range(2, num):
#         if num % i == 0: return False
#     return True

MAX = 50001
def get_prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return set([i for i in range(2, n) if sieve[i] == True])

prime_list = get_prime_list(MAX)
def solve(pos, nums, cnt, sum):
    res = 0
    if cnt > 3: return 0
    if pos == len(nums):
        if cnt == 3:
            # res += isPrime(sum)
            res += 1 if sum in prime_list else 0
        return res
    res += solve(pos+1, nums, cnt+1, sum+nums[pos])
    res += solve(pos+1, nums, cnt, sum)
    return res
def solution(nums):
    return solve(0, nums, 0, 0)

# print(solution(	[1, 2, 7, 6, 4]))