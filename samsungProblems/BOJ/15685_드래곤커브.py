# https://www.acmicpc.net/problem/15685
dd = [(0, 1), (-1, 0), (0, -1), (1, 0)]
MAX = 101
directions = [0]
#20세대 드래곤 커브 방향 기본으로 만들어 놓음
for i in range(20):
    prevDragonLen = len(directions)
    for j in range(prevDragonLen-1, -1, -1):
        directions.append((directions[j]+1)%4)

grid = [[0]*MAX for _ in range(MAX)]
#x, y 방향 대충보고 풀다 헤맴 문제좀 잘 읽죠 ㅜㅜ
for n in range(int(input())):
    y, x, d, g = map(int,input().split())
    grid[x][y] = 1
    for i in range(1<<g):
        dx, dy = dd[(directions[i]+d)%4]
        x, y = x+dx, y+dy
        grid[x][y] = 1

res = 0
for i in range(MAX-1):
    for j in range(MAX-1):
        if grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1]: res+=1
print(res)
