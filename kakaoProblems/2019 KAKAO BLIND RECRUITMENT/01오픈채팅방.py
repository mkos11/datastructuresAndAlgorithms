# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3

def solution(records):
    id_list = {}
    for info in records:
        info = info.split()
        if len(info) > 2:
            id_list[info[1]] = info[2]
    ans = []
    for record in records:
        info = record.split()
        nickname = id_list[info[1]]
        if info[0][0] == 'E':
            ans.append(f'{nickname}님이 들어왔습니다.')
        elif info[0][0] == 'L':
            ans.append(f'{nickname}님이 나갔습니다.')
    return ans
print(solution(	["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))