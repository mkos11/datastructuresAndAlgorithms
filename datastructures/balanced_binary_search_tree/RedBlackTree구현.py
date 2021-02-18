
# 얘도 BST 먼저 짜고 규칙 찾아보고 다시 짜보기

'''
정의
1. 각 노드 Red or Black
2. 루트노드는 Black
3. 모든 리프노드(NIL 노드)는 Black
4. Red노드의 자식 노드들은 전부 Black(즉, Red노드는 연속되어 등장하지 않음)
5. 모든 노드에 대해 그 노드로부터 자손인 리프노드에 이르는 모든 경로에는 동일한 개수의 Black 노드 존재
'''
# 레드블랙트리 경우의 수 많잖아 이건 그때그때 다시 공부하고 구현하기
# 루트 부모, 모든 리프노드 => NIL노드로 가정 그냥 None으로 처리하면 될듯

# push() -> 일반 BST처럼 삽입하고, 새로운 노드 z를 Red노드로, insertFixup() 만들어놓고 호출 해줘야함
'''
# insertFixup() -> 위반 가능성: 2번째 조건(근데 2번 조건은 그냥 루트를 블랙으로 바꿔주면 됨), 
# 4번 조건이 문제가 됨
# 반복 : 부모 y, 현재 z라 할 때, Red - Red 이면 부모노드 p[z]가 Black 될 때 종료(만약 조건 2 위반이면 z를 블랙으로 바꿔주고 종료)
insertFixup()
case (1, 2, 3)은 p(z)가 p(p[z])의 왼쪽 자식, (4, 5, 6)은 오른쪽 자식으로 대칭이므로 1, 2, 3만 볼거
case 1:
    - z의 삼촌이 red (부모 레드고, 할아버지는 자연스레 블랙, 그 다른 자식인 삼촌이 레드인 경우)
    - 부모, 삼촌 블랙으로 바꿔주고 할아버지 레드로 바꾸고 할아버지 노드를 새로운 z로 처리해줌
case 2:
    - z의 삼촌이 black, z가 p[z]의 오른쪽 자식
    - 부모에 대해서 left-rotation해줌. (p[z]가 z가 됨), 그러면 case 3이 됨
case 3:
    - z의 삼촌이 black, z가 p[z]의 왼쪽 자식
    - 부모 노드를 black, 할아버지 노드를 red로 바꾼 후 할아버지에 대해 right-rotation
'''

# pop() -> 삭제도 그냥 BST처럼 하고, 삭제되는 노드가 black인 경우 deleteFixup() 만들어놓고 호출 해줘야함
'''
# deleteFixup() -> 위반 가능성: 2번째 조건(2번은 그냥 루트 블랙으로 바꿔주면 됨), 4번(부모, 자식 모두 레드 => 그냥 자식 블랙 바꿔주면 됨)
# 5번째 조건이 문제가 됨 
# 노드 x(삭제하는 노드의 자식)에 "extra black"을 부여해서 일단 조건 5를 만족시켜줌
# 노드 x는 "double black" or "red & black"
# 반복 : extra black을 위로 올려보냄, red & black 되면 black 만들고 끝내고, x가 루트가 되면 extra black 제거하고 끝냄
deleteFixup()
case (1, 2, 3, 4)는 x(삭제하고 대체되는 노드)가 부모의 왼쪽, (5, 6, 7, 8)은 x가 부모의 오른쪽으로 대칭이므로 1, 2, 3, 4만 볼거
case 1:
    - x의 형제노드 w가 red
    - w를 black으로, 부모노드를 red로(swap)
    - 부모노드에 대하여 left-rotation
    - 이렇게 하면 다른 case로 넘어감
case 2: 
    - w가 black, w의 자식들도 black
    - x의 extra-black을 뺏고, w를 red로 바꿈
    - 부모노드에게 뺏은 extra-black을 줌
    - 부모를 새로운 x로
case 3:
    - w가 black, w의 왼쪽자식이 red
    - w를 red로, w의 왼쪽 자식을 black으로(swap)
    - w에 대하여 right-rotation
    - 이렇게 하면 x의 새로운 형제 w는 오른자식이 red인 case 4에 해당함
case 4:
    - w가 black, w의 오른쪽 자식이 red
    - w의 색을 x의 부모의 색으로, w의 오른자식을 black으로
    - x의 부모에 대하여 left-rotation
    - x의 extra-black을 제거하고 종료
'''
BLACK = True
RED = False
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.parent = None
        self.color = RED

class RedBlackTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return self.printTree("", self.root, False)
    def printTree(self, prefix, node, isLeft):
        res = ""
        if node is not None:
            res += f"{prefix}" + ("|-- " if isLeft else "\\-- ") + f"{node.data}\n"
            res += self.printTree(prefix + ("|   " if isLeft else "    "), node.left, True)
            res += self.printTree(prefix + ("|   " if isLeft else "    "), node.right, False)
        return res

    def push(self, data):
        self.root = self._push(self.root, data)
    def _push(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._push(node.left, data)
        else:
            node.right = self._push(node.right, data)
        return node

    def pop(self, data):
        self.root, deletedNode = self._pop(self.root, data)
        return deletedNode
    def _pop(self, node, data):
        deletedNode = None
        if node is None: return node, deletedNode
        if data == node.data:
            deletedNode = node
            if node is None: node = None
            elif node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            # node.left or node.right
            else:
                node = node.left or node.right
        elif node.data < data:
            node.left = self._pop(node.left, data)
        else:
            node.right = self._pop(node.right, data)
        return node, deletedNode

if __name__ == "__main__":
    redBlackTree = RedBlackTree()
    data = [i for i in range(1, 16)]
    for x in data: redBlackTree.push(x)
    print(redBlackTree)
    for x in data[:-5]: redBlackTree.pop(x)
    print(redBlackTree)