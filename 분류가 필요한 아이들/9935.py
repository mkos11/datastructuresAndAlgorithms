# https://www.acmicpc.net/problem/9935
# 스택
from sys import*
input = lambda:stdin.readline().rstrip()

string = input()
t = input()
st = []
t_size = len(t)
for c in string:
    st.append(c)
    st_size = len(st)
    if st_size >= t_size:
        if ''.join(st[st_size-t_size:]) == t:
            for i in range(t_size):
                st.pop()
print(''.join(st) if st else 'FRULA')