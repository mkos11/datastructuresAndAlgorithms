from sys import*
setrecursionlimit(10**6)
input = stdin.readline
MAX = 41
def fibo(n, mem, target):
    if n <= 1:
        if n == target: return 1
        return 0
    if mem[n] != -1: return mem[n]
    mem[n] = fibo(n-1, mem, target) + fibo(n-2, mem, target)
    return mem[n]
zero = [-1] * MAX
one = [-1] * MAX
zero[0], zero[1], one[0], one[1] = 1, 0, 0, 1
fibo(MAX-1, zero, 0)
fibo(MAX-1, one, 1)
for tc in range(int(input())):
    x = int(input())
    print(zero[x], one[x])
