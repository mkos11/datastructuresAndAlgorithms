def hanoi(cnt, a, b, c):    #from by to
    if cnt == 1:
        print(a, c)
        return
    hanoi(cnt-1, a, c, b)
    print(a, c)
    hanoi(cnt-1, b, a, c)
    return
n=int(input())
res = 0
for i in range(n):
    res += (1 << i)
print(res)
if n <= 20: hanoi(n, 1, 2, 3)
