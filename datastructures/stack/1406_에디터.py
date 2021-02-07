from sys import*
input = lambda:stdin.readline().strip()
a = input()
left, right = [], []
for i in range(len(a)):
    left.append(a[i])
for i in range(int(input())):
    commands = list(map(str,input().split()))
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
