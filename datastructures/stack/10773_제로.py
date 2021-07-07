# https://www.acmicpc.net/problem/10773
# 숫자를 하나씩 써내려가면서 0이 나오면 마지막 수를 지우고 싶음 스택이 딱이얌
from sys import *

input = stdin.readline

stack = []
for i in range(int(input())):
    num = int(input())
    if not num:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
