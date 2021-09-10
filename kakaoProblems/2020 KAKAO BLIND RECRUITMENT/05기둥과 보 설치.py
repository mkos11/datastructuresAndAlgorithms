# https://programmers.co.kr/learn/courses/30/lessons/60061
# 0, 1로 주어지면 상수로 알아보기 쉽게 바꿔주기
# 좌표 헷갈리면 그려보는게 최고
WIDTH, HEIGHT = 1, 0
def can_add(x, y, a, build):
    if a == HEIGHT: return x == 0 or (x, y-1, WIDTH) in build or (x, y, WIDTH) in build or (x-1, y, HEIGHT) in build
    return (x-1, y, HEIGHT) in build or (x-1, y+1, HEIGHT) in build or ((x, y-1, WIDTH) in build and (x, y+1, WIDTH) in build)
def solution(n, build_frame):
    build_set = set()
    for y, x, a, build in build_frame:
        if build:
            if can_add(x, y, a, build_set): build_set.add((x, y, a))
        else:
            build_set.remove((x, y, a))
            for bx, by, ba in build_set:
                if not can_add(bx, by, ba, build_set):
                    build_set.add((x, y, a))
                    break
    # 이 부분 람다식으로 처리 가능할거 같은데?
    ans = []
    for x, y, a in build_set:
        ans.append([y, x, a])
    return sorted(ans)
# print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))