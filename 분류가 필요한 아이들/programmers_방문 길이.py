# https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    n = 5
    dir_set = set()
    dd = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D':(1, 0)}
    reverse_dir = {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U'}
    ans, x, y = 0, 0, 0
    for dir in dirs:
        dx, dy = dd[dir]
        nx, ny = x + dx, y + dy
        if nx < -n or ny < -n or nx > n or ny > n: continue
        dir_set.add((x, y, dir))
        dir_set.add((nx, ny, reverse_dir[dir]))
        x, y = nx, ny
    return len(dir_set)//2
print(solution("ULURRDLLU"))