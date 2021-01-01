#https://www.acmicpc.net/problem/3986
from sys import*
input=lambda:stdin.readline().strip()
def checking(string):
    stack = []
    for i in range(len(string)):
        if len(stack)==0: stack.append(string[i])
        else:
            if string[i] == stack[-1]: stack.pop()
            else: stack.append(string[i])
    if not stack: return 1
    return 0

res = 0
for i in range(int(input())):
    if checking(input()): res+=1
print(res)