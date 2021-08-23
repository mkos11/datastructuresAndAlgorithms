# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

def solution(n, users):
    answer = []
    arrived_player = len(users)
    stages = [0] * (n + 2)
    for user in users:
        stages[user] += 1
    for i in range(1, n + 1):
        not_cleared_player = stages[i]
        answer.append((i, (not_cleared_player/arrived_player) if arrived_player != 0 else 0))
        arrived_player -= stages[i]
    return list(map(lambda x: x[0], (sorted(sorted(answer), key=lambda x: x[1], reverse=True))))

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))