# n과m(11)
# https://www.acmicpc.net/problem/15665

def solve(cnt):
    if cnt == m:
        for i in range(m):
            print(stack[i], end=' ')
        print()
        return
    prev = -1
    for i in range(n):
        if prev != arr[i]:
            stack.append(arr[i])
            solve(cnt+1)
            stack.pop()
            prev = arr[i]
n, m = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
stack = []
solve(0)

'''
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
        stack.append(arr[i])
        solve(cnt+1)
        stack.pop()

n, m = map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
dic = {}
stack = []
solve(0)
for key, value in dic.items():
    for x in key:
        print(x, end=' ')
    print()
'''