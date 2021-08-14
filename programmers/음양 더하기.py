# https://programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    ans = 0
    for i, absolute in enumerate(absolutes):
        ans += absolute if signs[i] else -absolute
    return ans

print(solution([4, 7, 12], [True, False, True]))