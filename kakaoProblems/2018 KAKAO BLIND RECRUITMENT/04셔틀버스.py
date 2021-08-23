# https://programmers.co.kr/learn/courses/30/lessons/17678
def padding(x):
    return ('0' + str(x)) if x < 10 else x
def solution(n, t, m, timetable):
    for i in range(len(timetable)):
        hour, minute = timetable[i].split(':')
        timetable[i] = int(hour) * 60 + int(minute)
    timetable.sort()
    idx = 0
    time = 540
    for i in range(n-1):
        for j in range(m):
            # 태움
            if len(timetable) > idx and time >= timetable[idx]:
                idx += 1
            else:
                break
        time += t
    if len(timetable) - idx >= m:
        last_crew = timetable[idx + m - 1]
        if last_crew <= time:
            time = last_crew - 1
    return f'{padding(time//60)}:{padding(time%60)}'

# print(solution(	1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
# print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
# print(solution(	2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
# print(solution(	1, 1, 1, ["23:59"]))
# print(solution(	10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))