# https://www.acmicpc.net/problem/15683
def detect(x, y, d):
    global room
    dx, dy = dd[d]
    while 1:
        x, y = x+dx, y+dy
        if x<0 or y<0 or x>n-1 or y>m-1 or room[x][y]==6: return
        if not room[x][y]: room[x][y]=9
def solve(pos):
    global room
    res = INF
    if pos == len(cctvList):
        blindSpot = 0
        for i in range(n):
            for j in range(m):
                if not room[i][j]:
                    blindSpot += 1
        return min(res, blindSpot)
    temp = [r[:] for r in room]
    x, y = cctvList[pos]
    for canMove in cctvDirections[room[x][y]]:
        #4방향 가도 될런지 살펴볼거
        for i in range(4):
            if (canMove & (1<<i)):
                detect(x, y, i)
        res = min(res, solve(pos+1))
        room = [t[:] for t in temp]
    return res

INF = int(1e9)
U, R, D, L = 1, 2, 4, 8     #비트연산자 사용할거라
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cctvDirections = [0,
                  [U, R, D, L],
                  [U|D, L|R],
                  [U|R, R|D, D|L, L|U],
                  [U|R|D, R|D|L, D|L|U, L|U|R],
                  [U|R|D|L],
                  ]
n, m = map(int,input().split())
room = [list(map(int,input().split()))for _ in range(n)]
cctvList = []
for i in range(n):
    for j in range(m):
        if 1 <= room[i][j] <= 5: cctvList.append((i, j))
print(solve(0))