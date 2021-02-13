# 부모 - 자식 간 크고 작음 보장
# 삽입은 맨 끝에 하고 자리 찾아가게 하고
# 삭제는 루트 자리에 마지막 원소 갖다놓고 원래 있던 루트 리턴해주면 될듯, 갖다놓은 애 자리 찾아가게 하고
# 삭제 진행하는 순서는 짜면서 생각해보기

# complete binary tree라 보통 배열에 구현하는데 여기선 링크드 리스트 이용해보기
# 그러려니까 마지막에 원소 추가하는게 문제네? 어떻게 하면 좋을지 고민해보기
# 마지막 원소에 추가해주려면 인덱스가 의미가 있어가지고 배열로 크기 정해놓고 짜는게 싫은거면 dict() or list 이용해서 짜기

# MIN heap으로 구현
class Heap:
    def __init__(self):
        self.heap = [None]  # 0 None 넣어놓고
        self.lastIdx = 0

    def __str__(self):
        return str(self.heap[1:])

    def push(self, data):
        self.heap.append(data)
        self.lastIdx += 1
        idx = self.lastIdx
        while idx > 1 and self.heap[idx//2] > self.heap[idx]:
            self.heap[idx], self.heap[idx//2] = self.heap[idx//2], self.heap[idx]
            idx //= 2

    def pop(self):
        if self.isEmpty(): return None
        # root랑 마지막 원소랑 바꾸고, 루트에 있는 애 자리 찾아줌
        self.heap[1], self.heap[self.lastIdx] = self.heap[self.lastIdx], self.heap[1]
        self.lastIdx -= 1
        deletedData = self.heap.pop()
        self.heapify()
        return deletedData

    # root원소 제자리 찾아가는 함수
    def heapify(self):
        parent = 1
        # 자식이 있으면 반복
        while( parent * 2 <= self.lastIdx ):
            left = parent * 2
            right = parent * 2 + 1
            # 자식 하나인 경우
            if left == self.lastIdx:
                if self.heap[left] >= self.heap[parent]: break
                self.heap[left], self.heap[parent] = self.heap[parent], self.heap[left]
                parent = left
            # 자식 둘인 경우
            else:
                if self.heap[left] >= self.heap[parent] and self.heap[right] >= self.heap[parent]: break
                if self.heap[left] < self.heap[right]:
                    self.heap[left], self.heap[parent] = self.heap[parent], self.heap[left]
                    parent = left
                else:
                    self.heap[right], self.heap[parent] = self.heap[parent], self.heap[right]
                    parent = right

    def isEmpty(self):
        return False if self.lastIdx else True

if __name__ == "__main__":
    heap = Heap()
    for x in [3, 1, 5, -2, 8, -13]:
        heap.push(x)
    print(heap)
    print(heap.pop())
    print(heap)
    print(heap.pop())
    print(heap)
    print(heap.pop())
    print(heap)