def dp(x):
    if x <= 2: return x
    if mem[x] != -1: return mem[x]
    mem[x] = (dp(x-2) + dp(x-1))%DIV
    return mem[x]
DIV = int(1e4) + 7
n=int(input())
mem = [-1] * (n+1)
print(dp(n))
