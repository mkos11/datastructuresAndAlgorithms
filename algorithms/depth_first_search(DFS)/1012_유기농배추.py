# https://www.acmicpc.net/problem/1012
from sys import*
input = stdin.readline
# 파이썬 기본 재귀 깊이 1000이라 재귀형태 사용할 때 주의, 1000넘어갈거 같으면 sys.setrecursionlimit() 선언해서 늘려줘야함
setrecursionlimit(10**6)

def dfs(x, y):
    visit[x][y] = 1
    '''
    아랫 부분 
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    글로벌로 선언해놓고
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
    이런식으로도 가능
    '''
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>m-1 or visit[nx][ny] or not board[nx][ny]: continue
        visit[nx][ny]=1
        dfs(nx, ny)
for tc in range(int(input())):
    m, n, k = map(int,input().split())
    board = [[0]*m for _ in range(n)]
    visit = [[0]*m for _ in range(n)]
    res = 0
    for i in range(k):
        # x를 행으로 쓰고 y를 열로 쓸건데 이 문제는 열,행 순서로 입력이 주어짐
        y, x = map(int,input().split())
        board[x][y] = 1
    for i in range(n):
        for j in range(m):
            # 아직 방문하지 않았고, 배추가 심어져 있는 곳(1인곳)
            if not visit[i][j] and board[i][j]:
                dfs(i, j)
                res += 1
    print(res)