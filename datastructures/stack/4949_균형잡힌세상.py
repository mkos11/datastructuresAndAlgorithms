# https://www.acmicpc.net/problem/4949
# 9012 괄호 업그레이드 버전
from sys import*
input=lambda:stdin.readline().rstrip()

def convert(c):
    if c=='(':return ')'
    else: return ']'

def checking(string):
    stack = []
    for i in range(len(string)):
        if string[i]=='(' or string[i]=='[': stack.append(convert(string[i]))
        elif string[i]==']' or string[i]==')':
            if not stack or (stack[-1] != string[i]): return 'no'
            stack.pop()
    if stack: return 'no'
    return 'yes'

while True:
    string = input()
    if string == '.': break
    print(checking(string))