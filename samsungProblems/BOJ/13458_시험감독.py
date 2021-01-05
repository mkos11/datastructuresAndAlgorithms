# https://www.acmicpc.net/problem/13458

n=int(input())
clients = list(map(int,input().split()))
master, manager = map(int,input().split())
res = 0
for i in range(n):
    res += 1
    clients[i] -= master
    if clients[i] >= 0:
        quotient = clients[i] // manager
        if clients[i]/manager == quotient:
            res += quotient
        else:
            res += quotient + 1
print(res)
