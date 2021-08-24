# https://programmers.co.kr/learn/courses/30/lessons/72410
alp = 'abcdefghijklmnopqrstuvwxyz-_.0123456789'
def end_dot_remove(new_id):
    for i in range(len(new_id)-1, -1, -1):
        if new_id[i] != '.':
            return new_id[:i+1]
    return ''
def solution(new_id):
    new_id = new_id.lower()

    temp = ''
    for c in new_id:
        if c not in alp: continue
        temp += c

    new_id = ''
    prev = '.'
    for c in temp:
        if prev == '.' and c == '.': continue
        new_id += c
        prev = c

    new_id = end_dot_remove(new_id)

    if new_id == '': new_id = 'a'

    if len(new_id) >= 16: new_id = end_dot_remove(new_id[:15])

    if len(new_id) <= 2: new_id += (new_id[-1] * (3 - len(new_id)))
    return new_id
# print(solution(	"...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))