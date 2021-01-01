#https://www.acmicpc.net/problem/9012
from sys import*
input=lambda:stdin.readline().strip()

def checking(string):
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        elif string[i] == ')':
            if not stack: return 'NO'
            else: stack.pop()
    if not stack: return 'YES'
    else: return 'NO'

for tc in range(int(input())):
    print(checking(input()))

''' 그냥 숫자 세어줘도 됨
from sys import*
input=lambda:stdin.readline().strip()
def checking(string):
    openParenthesisCnt = 0
    for i in range(len(string)):
        if string[i] == '(':
            openParenthesisCnt += 1
        elif string[i] == ')':
            if openParenthesisCnt <= 0: return 'NO'
            else: openParenthesisCnt -= 1
    if openParenthesisCnt == 0: return 'YES'
    return 'NO'
            
for tc in range(int(input())):
    print(checking(input()))
'''