# https://www.acmicpc.net/problem/14501
INF = 1e9
def solve(pos, price):
    res = 0
    if pos > n: return -INF
    if pos == n: return price
    res = max(res, solve(pos+days[pos], price + prices[pos]), solve(pos+1, price))
    return res
n=int(input())
days, prices = [], []
for i in range(n):
    d, p = map(int,input().split())
    days.append(d)
    prices.append(p)

print(solve(0, 0))