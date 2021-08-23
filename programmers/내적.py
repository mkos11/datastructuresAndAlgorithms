# https://programmers.co.kr/learn/courses/30/lessons/70128
def solution(a, b):
    ans = 0
    for i in range(len(a)):
        ans += (a[i] * b[i])
    return ans

print(solution(	[1, 2, 3, 4], [-3, -1, 0, 2]))