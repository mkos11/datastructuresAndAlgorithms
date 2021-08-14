# https://programmers.co.kr/learn/courses/30/lessons/83201
def grade(score):
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 50: return 'D'
    return 'F'
def solution(scores):
    INF = int(1e9)
    answer = ''
    for i in range(len(scores[0])):
        MAX = -INF
        MIN = INF
        total = 0
        for j in range(len(scores)):
            if i == j: continue
            data = scores[j][i]
            total += data
            if MAX < scores[j][i]: MAX = data
            if MIN > scores[j][i]: MIN = data
        cnt = len(scores) - 1
        if not(scores[i][i] > MAX or scores[i][i] < MIN):
            total += scores[i][i]
            cnt += 1
        answer += grade(total/cnt)
    return answer

print(solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))