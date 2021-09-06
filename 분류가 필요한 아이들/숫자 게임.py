def solution(A, B):
    a, b = 0, 0
    ans = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            ans += 1
            b += 1
        a += 1
    return ans