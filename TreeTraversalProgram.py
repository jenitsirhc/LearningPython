class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.node = data

def Preorder(root):
    if root:
        print(root.node)
        Preorder(root.left)
        Preorder(root.right)

root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(8)
root.right = Node(14)
root.right.left = Node(12)
root.right.right = Node(16)

print("Preorder traversal of the binary tree is: ")

Preorder(root)

def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.node)

root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(8)
root.right = Node(14)
root.right.left = Node(12)
root.right.right = Node(16)

print("")
print("Postorder traversal of the binary tree is: ")
Postorder(root)

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.node)
        Inorder(root.right)

root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(8)
root.right = Node(14)
root.right.left = Node(12)
root.right.right = Node(16)

print("")
print("Inorder traversal of the binary tree is :")

Inorder(root)

