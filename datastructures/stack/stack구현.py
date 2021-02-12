# 파이썬에서 top 변수로 두고 배열 만들어서 쓰는게 맞는건가 싶다
# 그렇게 짜는건 자바로 짤 때 짜고 여기선 그냥 파이썬 기본 문법 이용하기

# 단축키 tip(windows)
'''
라인 복사 ctrl + d
라인 삭제 ctrl + y
라인 합치기 ctrl + shift + j
라인 옮기기 ctrl + shift + 위 or 아래
이름 일괄 변경 shift + F6
import 정리 ctrl + alt + o
자동완성 ctrl + shift + space
코드 자동 정렬 ctrl + alt + l
'''
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def top(self):
        return self.stack[-1] if not self.isEmpty() else None

    def pop(self):
        return self.stack.pop() if not self.isEmpty() else None

    def isEmpty(self):
        return False if self.getSize() else True

    def getSize(self):
        return len(self.stack)

if __name__ == '__main__':
    stack = Stack()
    print(stack.isEmpty())
    stack.push(10)
    print(stack.isEmpty())
    print(stack.getSize())
    print(stack.top())
    print(stack.pop())
    print(stack.top())
    print(stack.pop())

