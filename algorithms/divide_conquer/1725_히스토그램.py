from sys import*
input=stdin.readline

def solve(start, end):
    if start == end: return h[start]
    mid = (start + end)//2
    res = max(solve(start, mid), solve(mid+1, end))
    left, right = mid, mid
    minH = h[mid]
    while right-left <= end-start:
        leftH, rightH = -1, -1
        if left-1 >= start:
           leftH = h[left-1]
        if right + 1 <= end:
            rightH = h[right+1]
        # 높이가 큰 방향으로 확장
        if leftH <= rightH:
            right+=1
            minH = min(minH, rightH)
        else:
            left-=1
            minH = min(minH, leftH)
        res = max(res, minH*(right-left+1))
    return res
n = int(input())
h = [int(input())for _ in range(n)]
print(solve(0, n-1))
