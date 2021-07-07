#https://www.acmicpc.net/problem/1918
# 후위 표기식2 문제에 괄호가 추가됨
# 피연산자는 출력(or 문자열 추가)
# 연산자는 우선순위에 따라 처리(스택 빌 때까지 or 스택 맨 위에 있는게 더 우선순위가 낮은거 일때까지 꺼냄)
# 괄호 => 짝궁 괄호 나올 때까지

stack = []
string = input()
priority = {'(':2, '*':1, '/':1, '+':0, '-':0}
res = ''
for i in range(len(string)):
    #피연산자면 출력
    if 'A' <= string[i] <= 'Z' or 'a' <= string[i] <= 'z': res += string[i]
    #닫힌 괄호면 열린거(짝꿍) 나올때까지 출력
    elif string[i] == ')':
        while stack:
            top = stack.pop()
            if top == '(':
                break
            else:
                res += top
    #나머지 연산자들 나왔을때
    else:   #연산자:: *, /, +, -, (
        while stack:
            if priority[stack[-1]] < priority[string[i]] or stack[-1] == '(':
                break
            else:
                res += stack.pop()
        stack.append(string[i])
#스택에 남은 연산자들 출력
while stack:
    res += stack.pop()
print(res)