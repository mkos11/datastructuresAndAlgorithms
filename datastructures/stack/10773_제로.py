#https://www.acmicpc.net/problem/10773
from sys import*
input=stdin.readline

stack = []
for i in range(int(input())):
    num = int(input())
    if not num: stack.pop()
    else: stack.append(num)

print(sum(stack))