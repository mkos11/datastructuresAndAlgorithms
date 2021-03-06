def dp(pos):
    if mem[pos] != -1: return mem[pos]
    mem[pos] = 0
    for i in range(pos+1, n):
        if arr[pos] < arr[i]:
            mem[pos] = max(mem[pos], dp(i)+1)
    return mem[pos]
n = int(input()) + 1
INF = int(1e9)
arr = [-INF] + list(map(int,input().split()))
mem = [-1] * n
print(dp(0))
