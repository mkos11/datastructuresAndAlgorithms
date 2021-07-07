# https://www.acmicpc.net/problem/1406
# linked list로 풀 수도 있음, 근데 스택 두개로도 풀 수 있음
# 왼쪽 스택, 오른쪽 스택 사이에 커서 있다고 생각하면 됨
# 커서에 따라서 왼쪽, 오른쪽으로 옮기고 마지막 출력은 (왼쪽 스택) + (오른쪽 스택역순)
from sys import*
input = lambda: stdin.readline().strip()
a = input()
left, right = [], []
for i in range(len(a)):
    left.append(a[i])
for i in range(int(input())):
    commands = list(map(str, input().split()))
    if commands[0] == 'L':
        if left:
            right.append(left.pop())
    elif commands[0] == 'D':
        if right:
            left.append(right.pop())
    elif commands[0] == 'B':
        if left:
            left.pop()
    elif commands[0] == 'P':
        left.append(commands[1])
print("".join(left) + "".join(right[::-1]))
