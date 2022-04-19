
# Creating the binary tree
# Create a Node Class
class Node:
    def __init__(self, val):
        self.childLeft = None
        self.childRight = None
        self.nodeData = val

# Populating the tree using the Node class
root = Node(5)
root.childLeft = Node(7)
root.childRight = Node(9)
root.childLeft.childLeft = Node(3)
root.childLeft.childRight = Node(11)
root.childRight.childLeft = Node(1)
root.childRight.childRight = Node(4)
root.childLeft.childRight.childLeft = Node(8)

# IN ORDER TRAVERSAL
print("IN-ORDER TRAVERSAL")
def InOrder(root):
    list = []
    if root:
        InOrder(root.childLeft)
        print(root.nodeData)
        InOrder(root.childRight)
InOrder(root)

# PRE-ORDER TRAVERSAL
print("PRE-ORDER TRAVERSAL")
def PreOrder(root):
    if root:
        print(root.nodeData)
        PreOrder(root.childLeft)
        PreOrder(root.childRight)
PreOrder(root)

# POST-ORDER TRAVERSAL
print("POST-ORDER TRAVERSAL")
def PostOrder(root):
    if root:
        PostOrder(root.childLeft)
        PostOrder(root.childRight)
        print(root.nodeData)
PostOrder(root)

