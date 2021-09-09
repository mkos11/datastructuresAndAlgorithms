# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    res = len(s)
    for size in range(1, len(s)//2 + 1):
        prev, cnt, length = s[:size], 1, 0
        for pos in range(size, len(s), size):
            curr = s[pos:pos+size]
            if prev == curr:
                cnt += 1
            else:
                if cnt != 1: length += len(str(cnt))
                length += size
                cnt = 1
            prev = curr
            if pos + size >= len(s):
                if pos + size > len(s):
                    length += (len(s) - pos)
                else:
                    length += size + (len(str(cnt)) if cnt != 1 else 0)
        res = min(res, length)
    return res

# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))