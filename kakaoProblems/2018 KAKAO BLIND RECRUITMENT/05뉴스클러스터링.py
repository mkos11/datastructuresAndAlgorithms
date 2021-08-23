# https://programmers.co.kr/learn/courses/30/lessons/17677
MUL = 65536
def make_set(string):
    res = set()
    cnt = {}
    for i in range(len(string) - 1):
        word = string[i:i + 2].lower()
        if word.isalpha():
            if word not in cnt:
                cnt[word] = 0
            else:
                cnt[word] += 1
            # parameter 'str'로 받고 str(cnt[word]) 해서 에러 났었음.. 예약어 변수명 쓸 때 조심하기
            res.add(word + f'{cnt[word]}')
    return res
def solution(str1, str2):
    set1 = make_set(str1)
    set2 = make_set(str2)
    return int((len(set1 & set2) / len(set1 | set2)) * MUL) if len(set1 | set2) != 0 else MUL

print(solution(	"aa1+aa2", "AAAA12"))