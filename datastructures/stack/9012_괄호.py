# #https://www.acmicpc.net/problem/9012
def is_vps(string):
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        elif string[i] == ')':
            if not stack:
                return 'NO'
            else:
                stack.pop()
    return 'NO' if stack else 'YES'

for tc in range(int(input())):
    print(is_vps(input()))

# https://www.acmicpc.net/problem/9012
# ()쌍이 되는 문자열 YES NO로 판단
# def is_vps(string):
#     cur = 0
#     for s in string:
#         if s == '(':
#             cur += 1
#         elif s == ')' and cur > 0:
#             cur -= 1
#         else:
#             return "NO"
#     return "YES" if cur == 0 else "NO"
#
#
# for i in range(int(input())):
#     print(is_vps(input()))
