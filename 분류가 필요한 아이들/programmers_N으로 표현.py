# https://programmers.co.kr/learn/courses/30/lessons/42895
from collections import*
def bfs(numbers, target):
    visit = {}
    q = deque()
    for number, cnt in numbers:
        visit[number] = cnt
        q.append(number)
    while q:
        u = q.popleft()
        if u == target: return visit[u]
        # +, -, *, // 네가지 연산을
        # numbers에 대해 모두 수행
        for number, cnt in numbers:
            if visit[number] + cnt > 8: break
            for v in [u + number, u * number, u // number, u - number]:
                if v in visit or v > target * 10: continue
                visit[v] = visit[u] + cnt
                q.append(v)
    return -1

def solution(n, target):
    numbers = []
    for i in range(1, len(str(target))+1):
        numbers.append([int(str(n)*i), i])
    return bfs(numbers, target)
print(solution(5, 12))