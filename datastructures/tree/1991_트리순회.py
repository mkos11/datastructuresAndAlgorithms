class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
def preOrder(node):
    if node is None: return
    print(node.val, end='')
    preOrder(nodes[node.left])
    preOrder(nodes[node.right])
def inOrder(node):
    if node is None: return
    inOrder(nodes[node.left])
    if node.val != '.': print(node.val, end='')
    inOrder(nodes[node.right])
def postOrder(node):
    if node is None: return
    postOrder(nodes[node.left])
    postOrder(nodes[node.right])
    if node.val != '.': print(node.val, end='')
nodes = {}
for i in range(int(input())):
    v, l, r = map(str,input().split())
    nodes[v] = Node(v, l, r)
root = nodes['A']
nodes['.']=None
preOrder(root)
print()
inOrder(root)
print()
postOrder(root)

