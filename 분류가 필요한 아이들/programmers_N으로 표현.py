# https://programmers.co.kr/learn/courses/30/lessons/42895
INF = int(1e9)
n, num = 0, 0
def solution(N, number):
    global n, num
    n = N
    num = number
    res = dfs(0, 0)
    return res if res != INF else -1
def dfs(number, cnt):
    res = INF
    if cnt > 8: return INF
    if number == num: return cnt
    temp = 0
    for i in range(1, 9):
        temp = temp * 10 + n
        res = min(res, dfs(number + temp, cnt + i))
        res = min(res, dfs(number * temp, cnt + i))
        res = min(res, dfs(number // temp, cnt + i))
        res = min(res, dfs(number - temp, cnt + i))
    return res
# print(solution(	5, 31168))
print(solution(	5, 12))