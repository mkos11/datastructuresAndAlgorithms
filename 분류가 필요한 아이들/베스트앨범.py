# https://programmers.co.kr/learn/courses/30/lessons/42579
# 처음에 class 만들어서 풀다가 코테에서는 빠르게 푸는게 더 중요한거 같아서 그냥 정렬하기 편한 리스트로 풂

def solution(genres, plays):
    dic = {}
    res = []
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = [0, []]
        dic[genres[i]][0] += plays[i]
        dic[genres[i]][1].append((i, plays[i]))
    for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True):
        v[1] = sorted(sorted(v[1]), key=lambda x: x[1], reverse=True)
        for i in range(min(2, len(v[1]))):
            res.append(v[1][i][0])
    return res
solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])