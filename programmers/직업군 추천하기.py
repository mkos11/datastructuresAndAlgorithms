# https://programmers.co.kr/learn/courses/30/lessons/84325
# 리뷰 하면서 zip 써보기
def solution(tables, languages, preference):
    table_size = len(tables)
    scores = {}
    for table in tables:
        table = table.split()
        scores[table[0]] = {}
        for i, language in enumerate(table[1:]):
            scores[table[0]][language] = table_size - i
    answer = ''
    MAX = 0
    for key, value in scores.items():
        sum = 0
        for i in range(len(languages)):
            sum += (scores[key][languages[i]] if (languages[i] in scores[key]) else 0) * preference[i]
        if MAX < sum:
            MAX = sum
            answer = key
        elif MAX == sum:
            answer = min(answer, key)
    return answer

print(solution(	["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))