# n과m(9)
# https://www.acmicpc.net/problem/15663
def solve(cnt):
    if cnt == m:
        for i in range(n):
            if(used[i]):
                print(used[i], end=' ')
        print()
        return
    prev = -1
    for i in range(n):
        if not visit[i] and prev != arr[i]:
            visit[i] = 1
            used[cnt] = arr[i]
            solve(cnt+1)
            visit[i] = 0
            used[cnt] = 0
            prev = arr[i]
n, m = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
visit = [0]*n
used = [0]*n
solve(0)
'''
# 굳이 사전 안써도 풀수있을듯??
def solve(cnt):
    if cnt == m:
        temp=[]
        for i in range(m):
            temp.append(stack[i])
        temp = tuple(temp)
        if temp not in dic:
            dic[temp] = 1
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            stack.append(arr[i])
            solve(cnt+1)
            stack.pop()
            visit[i] = 0
n, m = map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
dic = {}
stack = []
visit=[0]*n
solve(0)
for key, value in dic.items():
    for x in key:
        print(x, end=' ')
    print()
'''