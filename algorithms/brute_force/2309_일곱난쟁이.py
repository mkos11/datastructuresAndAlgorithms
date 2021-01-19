# https://www.acmicpc.net/problem/2309
# 7개 고르는데 100이 되는 수
def solve(pos, cnt, total):
    # 데이터 약해서 가지치기 안해도 됨, 대신 2798 블랙잭은 해야함
    # if cnt > 7 or total > 100: return
    if pos == 9:
        if cnt == 7 and total == 100:
            picked.sort()
            for p in picked:
                print(p)
            exit()
        return
    picked.append(heights[pos])
    solve(pos+1, cnt+1, total+heights[pos])
    picked.pop()
    solve(pos+1, cnt, total)
heights = []
picked = []
for i in range(9):
    heights.append(int(input()))
solve(0, 0, 0)