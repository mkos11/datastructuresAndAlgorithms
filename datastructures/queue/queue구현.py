# 큐도 배열 이용한건 java서 구현하고 여기선 그냥 linked list로 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    # head로 빼고 tail로 추가해줄거
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
    def enqueue(self, data):
        if self.isEmpty():
            node = Node(data)
            self.tail = node
            self.head = node
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self):
        if self.isEmpty(): return None
        deletedData = self.head.data
        self.head = self.head.next
        self.size -= 1
        return deletedData

    def front(self):
        return None if self.isEmpty() else self.head.data

    def isEmpty(self):
        return False if self.getSize() else True

    def getSize(self):
        return self.size

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    print(queue.isEmpty())
    print(queue.getSize())
    print(queue.dequeue())
    print(queue.getSize())
    print(queue.front())
    print(queue.getSize())
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(30)
    print(queue.front())