# https://programmers.co.kr/learn/courses/30/lessons/17679?language=python3
def gravity(n, m, board):
    for y in range(m):
        temp = []
        for x in range(n):
            if board[x][y] != ' ':
                temp.append(board[x][y])
                board[x][y] = ' '
        for x in range(len(temp)):
            board[n-x-1][y] = temp[-(x+1)]
def solution(n, m, board):
    for i in range(len(board)):
        board[i] = list(board[i])
    ans = 0
    while True:
        visit = [[0]*m for _ in range(n)]
        removed = False
        for i in range(n-1):
            for j in range(m-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != ' ':
                    visit[i][j] = visit[i][j+1] = visit[i+1][j] = visit[i+1][j+1] = 1
                    removed = True
        if not removed: return ans
        for i in range(n):
            for j in range(m):
                if visit[i][j]:
                    board[i][j] = ' '
                    ans += 1
        gravity(n, m, board)
