# https://programmers.co.kr/learn/courses/30/lessons/60058
reverse = {'(':')', ')':'('}
def is_balance(s):
    return s.count('(') == s.count(')')
def is_correct(s):
    cnt = 0
    for c in s:
        if c == '(': cnt += 1
        else:
            if cnt <= 0: return False
            cnt -= 1
    return cnt == 0
def solution(s):
    if s == '': return ''
    u, v = s, ''
    for i in range(2, len(s), 2):
        if is_balance(s[:i]):
            u, v = s[:i], s[i:]
            break
    if is_correct(u):
        return u + solution(v)
    return '(' + solution(v) + ')' + ''.join(map(lambda x: reverse[x], u[1:-1]))
print(solution(	"(()())()"))