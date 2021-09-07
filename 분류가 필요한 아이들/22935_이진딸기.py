# https://www.acmicpc.net/problem/22935
LENGTH = 16
nums = []
num = 1
for i in range((LENGTH-2)*2):
    nums.append(num)
    if i < LENGTH-2: num += 1
    else: num -= 1
def solve(n):
    res = []
    n = nums[(n-1) % ((LENGTH-2)*2)]
    for i in range(4):
        if n % 2 == 1: res.append('딸기')
        else: res.append('V')
        n //= 2
    return ''.join(res[::-1])
for tc in range(int(input())):
    print(solve(int(input())))