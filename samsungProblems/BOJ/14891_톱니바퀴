# https://www.acmicpc.net/problem/14891
def turn(num, direction):
    global visit
    visit[num] = direction
    if num-1 >= 0 and visit[num-1]==0 and (cogwheels[num-1][2] != cogwheels[num][6]):
        turn(num-1, -direction)
    if num+1 < 4 and visit[num+1]==0 and (cogwheels[num][2] != cogwheels[num+1][6]):
        turn(num+1, -direction)
def rotate(visit):
    global cogwheels
    for i in range(4):
        if not visit[i]: continue
        temp = []
        if visit[i]==1:
            for j in range(8):
                temp.append(cogwheels[i][(j+7)%8])
        if visit[i]==-1:
            for j in range(8):
                temp.append(cogwheels[i][(j+1)%8])
        for j in range(8):
            cogwheels[i][j] = temp[j]
cogwheels = [list(input()) for _ in range(4)]
k=int(input())
for i in range(k):
    n, d = map(int, input().split())
    visit=[0]*4
    turn(n-1, d)
    rotate(visit)

res = 0
for i in range(4):
    if cogwheels[i][0] == '1': res += (1<<i)
print(res)
