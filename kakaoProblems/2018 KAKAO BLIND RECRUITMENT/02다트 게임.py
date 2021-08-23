# https://programmers.co.kr/learn/courses/30/lessons/17682
# SDT 다음으로 옵션인지 확인하는데, 없을수도 있어서 주어진 문자열에 ' ' 패딩 하고 하려함
# 아니 문제 푸는데 왜이리 집중을 못해 dartResult += ' ' 이 연산의 시간복잡도를 왜 찾아보고 있냐고
# 시간도 넉넉한 문젠데 제발 중요치 않은 거에 공들이지 말자 궁금하면 끝나고 찾아보라고,,
# 끝나고 모듈화!
def init():
    return '', '', ''
def solution(dartResult):
    bonus_dic = {'S': 1, 'D': 2, 'T': 3}
    dartResult += ' '
    scores = [0, 0, 0, 0]
    i = 0
    score_idx = 1
    score, bonus, option = init()
    while i < len(dartResult):
        if '0' <= dartResult[i] <= '9':
            score += dartResult[i]
        elif dartResult[i] in 'SDT':
            bonus = dartResult[i]
            score = int(score)
            scores[score_idx] = score ** bonus_dic[bonus]
            option = dartResult[i+1]
            if option == '*':
                scores[score_idx-1] *= 2
                scores[score_idx] *= 2
                i += 1
            elif option == '#':
                scores[score_idx] *= -1
                i += 1
            score_idx += 1
            score, bonus, option = init()
        i += 1
    print(scores)
    return sum(scores[1:])
print(solution("1T2D3D#"))
