# https://www.acmicpc.net/problem/22945
n = int(input())
arr = list(map(int, input().split()))
l, r = 0, n-1
res = 0
while l < r:
    # print(l, r, res)
    res = max(res, (r-l-1) * min(arr[l], arr[r]))
    if arr[l] < arr[r]:
        l += 1
    else:
        r -= 1
print(res)
