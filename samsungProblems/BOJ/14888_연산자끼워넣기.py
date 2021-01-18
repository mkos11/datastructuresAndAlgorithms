def solve(pos, res):
    global MAX, MIN
    if pos == n:
        MAX = max(MAX, res)
        MIN = min(MIN, res)
        return
    for i in range(4):
        if operators[i]:
            operators[i]-=1
            if i==0:
                solve(pos+1, res+operands[pos])
            if i==1:
                solve(pos+1, res-operands[pos])
            if i==2:
                solve(pos+1, res*operands[pos])
            if i==3:
                solve(pos+1, int(res/operands[pos]))
            operators[i]+=1
    return
n=int(input())
operands = list(map(int,input().split()))
#=-*/
operators = list(map(int,input().split()))
INF = int(1e10)
MAX, MIN = -INF, INF
solve(1, operands[0])
print(MAX, MIN, sep='\n')
