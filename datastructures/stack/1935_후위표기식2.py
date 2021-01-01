# https://www.acmicpc.net/problem/1935
from sys import*

# stdin = open("C:/projects/datastructuresAndAlgorithms/testInput.txt")
input=lambda:stdin.readline().strip()

def cal(x, op, y):
    if op == '+': return x+y
    if op == '*': return x*y
    if op == '-': return x-y
    if op == '/' and y!=0: return x/y
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpToInt = {}

n=int(input())
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