# https://www.acmicpc.net/problem/1062
def check(word, curr_set):
    for w in word:
        if w not in curr_set: return False
    return True
def cal():
    cnt = 0
    for word in word_list:
        # a.union(b) 연산 => O(len(a) + len(b)) 여기서 시간초과 남
        # if (word.union(curr_set)) == curr_set:
        #     cnt += 1
        
        # O(len(a))로 바꿔줌
        cnt += check(word, curr_set)
    return cnt

def solve(pos, cnt):
    res = 0
    if cnt >= k:
        return cal()
    for i in range(pos, len(alp)):
        if used[i]: continue
        used[i] = True
        curr_set.add(alp[i])
        res = max(res, solve(i, cnt + 1))
        used[i] = False
        curr_set.remove(alp[i])
    return res
alp = 'bdefghjklmopqrsuvwxyz'      #antic 제거
removed = 'antic'
n, k = map(int, input().split())
word_list = []
curr_set = set()
used = [False] * len(alp)
for i in range(n):
    temp = set()
    for c in input():
        if c in removed: continue
        temp.add(c)
    word_list.append(temp)
# antic 5개 제거
k -= 5
print(solve(0, 0))
# print(2**21)