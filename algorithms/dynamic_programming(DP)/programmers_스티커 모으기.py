# https://programmers.co.kr/learn/courses/30/lessons/12971
# dp
# prev == 0 이전 스티커 안뗌, 1 이전 스티커 뗌
from sys import *
setrecursionlimit(10 ** 6)
def solve(prev, pos, mem, sticker, first):
    if pos == len(sticker): return 0
    if mem[prev][pos] != -1: return mem[prev][pos]
    mem[prev][pos] = 0
    if prev == 0 and not (pos == len(sticker) - 1 and first):
        mem[prev][pos] += max(solve(0, pos+1, mem, sticker, first), solve(1, pos+1, mem, sticker, first) + sticker[pos])
    else:
        mem[prev][pos] += solve(0, pos+1, mem, sticker, first)
    return mem[prev][pos]
def solution(sticker):
    mem = [[-1] * len(sticker) for _ in range(2)]
    res1 = solve(0, 1, mem, sticker, 0)
    mem = [[-1] * len(sticker) for _ in range(2)]
    res2 = solve(1, 1, mem, sticker, 1) + sticker[0]
    # return max(solve(0, 1, mem, sticker, 0), solve(1, 1, mem, sticker, 1) + sticker[0])
    # print(mem)
    return max(res1, res2)

if __name__ == "__main__":
    print(solution([1, 3, 2, 5, 4]))
    # print(solution([14, 6, 5, 11, 3, 9, 2, 10]))