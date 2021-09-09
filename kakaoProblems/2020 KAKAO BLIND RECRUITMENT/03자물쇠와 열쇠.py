# https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3
def rotate(key):
    key_size = len(key)
    new_key = [[]for _ in range(key_size)]
    for i in range(key_size):
        for j in range(key_size):
            new_key[i].append(key[key_size - j - 1][i])
    return new_key
def compare(key, board, cnt, sx, sy):
    for x in range(len(key)):
        for y in range(len(key)):
            if board[sx + x][sy + y] == 2: continue
            if key[x][y] != board[sx + x][sy + y]:
                if board[sx + x][sy + y] == 0: cnt -= 1
            else:
                return False
    return cnt == 0
def can_open(key, board, zero_cnt):
    key_size = len(key)
    start_size = len(board) - key_size + 1
    for sx in range(start_size):
        for sy in range(start_size):
            if compare(key, board, zero_cnt, sx, sy): return True
    return False

def solution(key, lock):
    key_size, lock_size = len(key), len(lock)
    board_size = (key_size*2) + lock_size - 2
    board = [[2]*board_size for _ in range(board_size)]
    zero_cnt = 0
    for x in range(lock_size):
        for y in range(lock_size):
            if not lock[x][y]: zero_cnt += 1
            board[key_size - 1 + x][key_size - 1 + y] = lock[x][y]
    for i in range(4):
        if can_open(key, board, zero_cnt): return True
        key = rotate(key)
    return False
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))