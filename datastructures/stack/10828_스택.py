#https://www.acmicpc.net/problem/10828
from sys import*
input=lambda:stdin.readline().strip()

def isEmptyStack(stack):
    if not stack: return 1
    else: return 0

stack = []
for tc in range(int(input())):
    command = list(map(str, input().split()))
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if isEmptyStack(stack): print(-1)
        else: print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(isEmptyStack(stack))
    elif command[0] == 'top':
        if isEmptyStack(stack): print(-1)
        else: print(stack[-1])