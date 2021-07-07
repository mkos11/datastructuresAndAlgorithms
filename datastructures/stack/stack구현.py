# 파이썬에서 top 변수로 두고 배열 만들어서 쓰는게 맞는건가 싶다
# 그렇게 짜는건 자바로 짤 때 짜고 여기선 그냥 파이썬 기본 문법 이용하기
# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, data):
#         self.stack.append(data)
#
#     def top(self):
#         return self.stack[-1] if not self.isEmpty() else None
#
#     def pop(self):
#         return self.stack.pop() if not self.isEmpty() else None
#
#     def isEmpty(self):
#         return False if self.getSize() else True
#
#     def getSize(self):
#         return len(self.stack)

# top 써서 구현
class Stack:
    def __init__(self, size):
        self.stack = [None for _ in range(size)]
        self.top = -1
        self.max_size = size

    def push(self, data):
        if self.top + 1 > self.max_size: return 'overflow'
        self.top += 1
        self.stack[self.top] = data

    def peek(self):
        return self.stack[self.top] if not self.empty() else None

    def pop(self):
        if self.empty(): return None
        data = self.stack[self.top]
        self.top -= 1
        return data

    def empty(self):
        return False if self.top != -1 else True

    def size(self):
        return self.top + 1

if __name__ == '__main__':
    stack = Stack(101)
    print("empty:", stack.empty())
    stack.push(10)
    print("empty:", stack.empty())
    print("size:", stack.size())
    print("top:", stack.peek())
    print("pop:", stack.pop())
    print("top:", stack.peek())
    print("pop:", stack.pop())

