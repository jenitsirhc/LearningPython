
class NodeBST:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                   self.left = NodeBST(data)
                else:
                    self.left.insert(data)
                
            elif data > self.data:
                if self.right is None:
                   self.right = NodeBST(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print Tree

    def printTree(self):
        if self.left:
           self.left.printTree()
        
        print(self.data)
        if self.right:
           self.right.printTree()

    def inorderTraversal(self,root):
        res = []
        if root:
           res = self.inorderTraversal(root.left)
           res.append(root.data)
           res = res + self.inorderTraversal(root.right)
        return res

    def search(self, data):
        
        if self.data == data:
            print("The item that you are looking for is available")
            return
        
        if data < self.data:
            if self.left:
               self.search(data)
               return

            else:
                print("The item that you are looking for does not exist.")

        else:
            if self.right:
               self.right.search(data)
               return
            
            else:
                print("The item that you are looking for does not exist.")

