class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __str__(self):
        return f'\nstart: {self.start} end: {self.end}'
def cal(pivot_start, time_list):
    cnt = 0
    pivot_end = pivot_start + 1000
    for time in time_list:
        start, end = time.start, time.end
        if start <= pivot_start and pivot_end <= end: cnt += 1
        elif pivot_start <= end <= pivot_end: cnt += 1
        elif pivot_start <= start <= pivot_end: cnt += 1
    print(pivot_start, cnt)
    return cnt
def solution(lines):
    time_list = []
    res = 0
    for line in lines:
        day, response_time, processing_time = line.split()
        processing_time = float(processing_time[:-1]) * 1000
        hour, minute, second = map(float, response_time.split(':'))
        second *= 1000
        minute += (hour * 60)
        second += (minute * 60 * 1000)
        time_list.append(Node(int(second), int(second + processing_time)))
    print(*time_list)
    for time in time_list:
        print(time)
        res = max(res, cal(time.start, time_list), cal(time.end, time_list))
    return res
# print(solution(	["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))
print(solution(	["2016-09-15 20:59:57.421 0.351s",
                    "2016-09-15 20:59:58.233 1.181s",
                    "2016-09-15 20:59:58.299 0.8s",
                    "2016-09-15 20:59:58.688 1.041s",
                    "2016-09-15 20:59:59.591 1.412s",
                    "2016-09-15 21:00:00.464 1.466s",
                    "2016-09-15 21:00:00.741 1.581s",
                    "2016-09-15 21:00:00.748 2.31s",
                    "2016-09-15 21:00:00.966 0.381s",
                    "2016-09-15 21:00:02.066 2.62s"]))