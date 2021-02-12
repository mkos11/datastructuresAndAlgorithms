# 양방향으로 만들어볼까
# 삽입 기본은 맨 뒤에, 삽입할 곳 파라미터 주어지면 그 원소 찾아서 삽입하는 오버로딩 함수 만들면 될듯
# 삭제는 찾아서 삭제하도록?
# 그럼 head, tail로 처음과 끝 표시해두자
# 근데 원래 이렇게 복잡함? 예외처리 따로 해주지말고 tail None으로 처리하면 편하려나?
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def isEmpty(self):
        return False if self.getSize() else True

    def getSize(self):
        return self.size

    # 파이썬 함수 오버로딩 제공 안해준대! argument 여러개 받는식으로 해결
    def insert(self, *args):
        self.size += 1
        if len(args) == 1: self._insert(*args)
        else:
            self.head = self.searchInsert(self.head, *args)
    def _insert(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(data)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
    def searchInsert(self, node, data, searchData):
        # 마지막 노드면 그냥 삽입
        if node is self.tail:
            newNode = Node(data)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = self.tail.next
            return node
        # 중간에 삽입하는 거면 잘 연결해줌
        if node.data == searchData:
            newNode = Node(data)
            node.next.prev = newNode
            newNode.next = node.next
            newNode.prev = node
            node.next = newNode
            return node
        node.next = self.searchInsert(node.next, data, searchData)
        return node

    def delete(self, searchData):
        self.head, deletedNode = self._delete(self.head, searchData)
        if deletedNode is not None: self.size -= 1
        return deletedNode
    def _delete(self, node, searchData):
        deletedNode = None
        if node is None: return node, deletedNode
        if node.data == searchData:
            deletedNode = node
            # head면
            if node == self.head:
                if self.getSize() == 1:
                    self.head = self.tail = None
                else:
                    self.head = node.next
                return node.next, deletedNode
            # tail이면
            if node == self.tail:
                self.tail = node.prev
                return None, deletedNode
            # 중간이면
            node.prev.next = node.next
            node.next.prev = node.prev
            return node.next, deletedNode
        node.next, deletedNode = self._delete(node.next, searchData)
        return node, deletedNode

    def list(self):
        def _list(node):
            if node is None: return
            print(node, end=' ')
            _list(node.next)
        _list(self.head)
        print()
if __name__ == "__main__":
    linkedList = LinkedList()
    for x in [3, 4, 5, 6, 7]:
        linkedList.insert(x)
    linkedList.list()
    linkedList.insert(9, 3)
    linkedList.insert(10, 7)
    linkedList.insert(11, 5)
    linkedList.list()
    for x in [3, 10, 5, 5]:
        print(linkedList.delete(x))
    linkedList.list()
    for x in [9, 4, 11, 6, 7]:
        print(linkedList.delete(x))
    linkedList.list()
    print(linkedList.head, linkedList.tail)