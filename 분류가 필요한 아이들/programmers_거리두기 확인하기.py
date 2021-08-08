# https://programmers.co.kr/learn/courses/30/lessons/81302
from collections import*
n = 5
def check(board, i, j):
    visit = [[0]*n for _ in range(n)]
    visit[i][j] = 1
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1 or visit[nx][ny] or board[nx][ny]=='X': continue
            visit[nx][ny] = visit[x][y] + 1
            if visit[nx][ny] > 3: continue
            if board[nx][ny] == 'P': return 0
            q.append((nx, ny))
    return 1
def bfs(board):
    res = 1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'P':
                res &= check(board, i, j)
    return res
def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer