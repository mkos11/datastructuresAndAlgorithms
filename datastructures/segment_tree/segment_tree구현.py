from math import*

class SegmentTree:
    # 전체 크기는 그려보면 됨, 높이 h = log2(n)+1 이고(안나눠 떨어지면 올림 해줌), 개수는 두배씩 늘어나므로(full binary tree)
    # 그 개수를 높이와 비트연산으로 구해주면 1 << h
    # 루트가 하나라 (1 << h) - 1 아니야? 할수도 있지만, 1부터 시작할거라 None 하나 0에 껴넣을거임 그래서 딱맞음
    def __init__(self, data=None):
        if data is None: self.data = list(map(int, input("데이터 입력(공백을 기준으로 나눔)").split()))
        else: self.data = data
        n = len(self.data)
        h = ceil(log2(n)) + 1
        self.tree = [None] * (1 << h)
        self.init(1, 0, n - 1)

    def init(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
            return self.tree[node]
        mid = (start + end) // 2
        self.tree[node] = self.init(node * 2, start, mid) + self.init(node * 2 + 1, mid + 1, end)
        return self.tree[node]

    def update(self, targetNode, val):
        self._update(1, 0, len(self.data) - 1, targetNode, val)
    def _update(self, node, start, end, targetNode, val):
        # 범위 벗어남
        if not (start <= targetNode <= end): return self.tree[node]
        # base case, targetNode에 도착
        if start == end:
            self.tree[node] = val
            return self.tree[node]
        mid = (start + end) // 2
        # 재귀적으로 갱신된 값 다 처리해줌
        self.tree[node] = self._update(node * 2, start, mid, targetNode, val) + \
                          self._update(node * 2 + 1, mid + 1, end, targetNode, val)
        return self.tree[node]

    def cal(self, targetRangeLeft, targetRangeRight):
        return self._cal(1, 0, len(self.data) - 1, targetRangeLeft, targetRangeRight)
    def _cal(self, node, start, end, targetRangeLeft, targetRangeRight):
        # 범위 벗어남
        if targetRangeLeft > end or targetRangeRight < start: return 0
        # 범위에 챡 들어옴
        if targetRangeLeft <= start and end <= targetRangeRight: return self.tree[node]
        mid = (start + end) // 2
        return self._cal(node * 2, start, mid, targetRangeLeft, targetRangeRight) + \
               self._cal(node * 2 + 1, mid + 1, end, targetRangeLeft, targetRangeRight)

# 세그먼트 트리는 관련 문제 풀면서 테스트 하기
# https://www.acmicpc.net/problem/2042
from sys import*
input = stdin.readline
n, m, k = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))
segmentTree = SegmentTree(data)
for i in range(m+k):
    f, u, v = map(int, input().split())
    if f == 1: segmentTree.update(u-1, v)
    else: print(segmentTree.cal(u-1, v-1))