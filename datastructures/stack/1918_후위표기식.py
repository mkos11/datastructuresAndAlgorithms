#https://www.acmicpc.net/problem/1918

stack = []
string = input()
operator = {'(':2, '*':1, '/':1, '+':0, '-':0}
for i in range(len(string)):
    #피연산자면 출력
    if 'A' <= string[i] <= 'Z' or 'a' <= string[i] <= 'z': print(string[i],end='')
    #닫힌 괄호면 열린거(짝꿍) 나올때까지 출력
    elif string[i] == ')':
        while stack:
            top = stack.pop()
            if top == '(':
                break
            else:
                print(top, end='')
    #나머지 연산자들 나왔을때
    else:   #연산자:: *, /, +, -, (
        while stack:
            if operator[stack[-1]] < operator[string[i]] or stack[-1]=='(':
                break
            else:
                print(stack.pop(), end='')
        stack.append(string[i])
#스택에 남은 연산자들 출력
while stack:
    print(stack.pop(), end='')
