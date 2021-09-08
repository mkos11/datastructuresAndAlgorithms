# https://programmers.co.kr/learn/courses/30/lessons/68646
INF = int(1e9)
def solution(arr):
    n = len(arr)
    MIN = INF
    less_than = [0] * n
    for i in range(n):
        if MIN > arr[i]:
            MIN = arr[i]
        else:
            less_than[i] += 1
    MIN = INF
    for i in range(n-1, -1, -1):
        if MIN > arr[i]:
            MIN = arr[i]
        else:
            less_than[i] += 1
    # print(less_than)
    return len(list(filter(lambda x: x != 2, less_than)))

print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))