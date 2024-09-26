from binarytree import Node
from statistics import mean


#            10
#          /    \
#         5     14
#        / \   /  \
#       2   8 12  16




root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(8)
root.right = Node(14)
root.right.left = Node(12)
root.right.right = Node(16)

# Display the binary tree
print("Binary Tree   : ", root)

print("------------!Display!------------")

# Display all elements
print("Elements      : ", root.values)

# Display the level order of the nodes
print("Level Order   : ", root.levelorder)

# Display the inorder of the nodes
print("In Order      : ", root.inorder)

# Display the preorder of the nodes
print("Pre Order     : ", root.preorder)

# Display the postorder of the nodes
print("Post Order    : ", root.postorder)

# Display the size of the binary tree
print("Size          : ", root.size)

# Display the height of the binary tree
print("Height        : ", root.height)

# Display the minimum and maximum elements
print("Minimum       : ", root.min_node_value)

# Display the minimum and maximum elements
print("Maximum       : ", root.max_node_value)

# Display the sum of the elements
print("Sum           : ", sum(root.values))

# Display the average of the elements
print(f"Average       :  %0.2f"% mean(root.values))






