# https://www.acmicpc.net/problem/1935
# 1. A~Z 숫자로
# 2. 피연산자면 스택에 쌓고, 연산자면 스택 상위 두개 뽑아서 계산, 마지막 남은 수 출력
# 3. 계산하는 함수
from sys import*

input = lambda: stdin.readline().strip()

def cal(x, op, y):
    if op == '+': return x+y
    if op == '*': return x*y
    if op == '-': return x-y
    if op == '/' and y!=0: return x/y

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpToInt = {}

n = int(input())
inp = input()
for i in range(n):
    alpToInt[alp[i]] = int(input())

stack = []
for i in range(len(inp)):
    if 'A' <= inp[i] <= 'Z':
        stack.append(alpToInt[inp[i]])
    else:
        nxt = stack.pop()
        prev = stack.pop()
        stack.append(cal(prev, inp[i], nxt))
print('%.2f' %stack[0])