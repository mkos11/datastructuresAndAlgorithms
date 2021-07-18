# https://www.acmicpc.net/problem/11559
# 뿌요뿌요~
from collections import *
dd = [(0, 1), (0, -1), (-1, 0), (1, 0)]
def bfs(x, y, visit):
    q = deque()
    q.append((x, y))
    curr = board[x][y]
    visit[x][y] = True
    pop_list = [(x, y)]
    while q:
        x, y = q.popleft()
        for dx, dy in dd:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1 or visit[nx][ny] or board[nx][ny] != curr: continue
            visit[nx][ny] = True
            q.append((nx, ny))
            pop_list.append((nx, ny))
    if len(pop_list) < 4: return False
    for x, y in pop_list:
        board[x][y] = '.'
    return True
def gravity():
    for y in range(m):
        st = []
        for x in range(n):
            if board[x][y] == '.': continue
            st.append((board[x][y]))
            board[x][y] = '.'
        for x in range(n-1, -1, -1):
            if not st: break
            board[x][y] = st.pop()
def pop():
    visit = [[False]*m for _ in range(n)]
    can_pop = False
    for i in range(n):
        for j in range(m):
            if visit[i][j] or board[i][j] == '.': continue
            can_pop |= bfs(i, j, visit)
    return can_pop

def solve():
    res = 0
    while 1:
        if not pop(): return res
        gravity()
        res += 1
board = []
n, m = 12, 6
for i in range(n):
    board.append(list(input()))
print(solve())