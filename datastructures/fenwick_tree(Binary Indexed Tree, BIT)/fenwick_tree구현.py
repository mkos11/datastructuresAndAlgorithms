# (Binary Indexed Tree, BIT)
# segment tree 변형으로 메모리 절약!
# 반쪽씩만 저장해놓고 큰거에서 범위가 아닌부분 빼주는 식으로 구간합 구함

# 이걸 비트로 바라보면, (그림 그려서 확인하는게 최고)
# 구간합 구할 때 1이 있는 가장 오른쪽 비트(최하위 비트)가 0으로 바뀜
# 업데이트시에는 1이 있는 가장 오른쪽 비트에 1을 더해가며 구해주면 됨
# segment는 위에서 내려오면서 갱신한다면, fenwick은 아래에서 올라가면서 갱신

class FenwickTree:
    def __init__(self, data=None):
        # if type(data) == int: 이런식으로 받아서 처리도 가능
        if data is None: self.tree = [0] + list(map(int, input().split()))
        else: self.tree = [0] + data
        # 데이터 받아와서 한번에 초기화, dp식으로
        for idx in range(len(self.tree)):
            if idx + (idx & -idx) < len(self.tree):
                self.tree[idx + (idx & -idx)] += self.tree[idx]

    def __str__(self):
        return str(self.tree)

    def getSum(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            # 최하위 비트 지우기
            idx -= (idx & -idx)
        return res

    def interSum(self, left, right):
        return self.getSum(right) - self.getSum(left - 1)

    def update(self, idx, diff):
        while idx < len(self.tree):
            self.tree[idx] += diff
            # 최하위 비트 더해줌
            idx += (idx & -idx)

# 펜윅 트리도 관련 문제 풀면서 테스트 하기
# https://www.acmicpc.net/problem/2042
from sys import*
input = stdin.readline
n, m, k = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))
fenwickTree = FenwickTree(data)
for i in range(m+k):
    # print(fenwickTree)
    f, u, v = map(int, input().split())
    if f == 1:
        # 이 부분 때문에 고생함
        diff = v - fenwickTree.interSum(u, u)
        fenwickTree.update(u, diff)
    else:
        print(fenwickTree.interSum(u, v))
'''
54 line 추가 전 반례
5 2 1
1
2
3
4
5
1 1 5
1 2 4   여기서!!! 문제 발생
2 1 5
correct answer: 21
wrong answer: 16 
'''