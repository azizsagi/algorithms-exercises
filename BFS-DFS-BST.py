class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    def print_tree(self):
        if self.left:
            self.left.print_tree()        
        print(self.data)
        if self.right:
            self.right.print_tree()
        


    #Insertion
    def insert(self,value):
        if self.data:
           
            if value < self.data:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.data:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(self.insert(value))
        else:
            self.data = value
        

    # Binary Search Tree
    def BST_search(self, root,needle):
        if not root or root.data == needle:
            return root
        if needle < root.data:
            return self.BST_search(root.left, needle)
        if needle > root.data:
            return self.BST_search(root.right, needle)

    # In-order  Left -> Root -> Right
    def in_order(self,root):
            res = []
            if root:
                res = self.in_order(root.left)
                res.append(root.data)
                res = res + self.in_order(root.right)

            return res

    # Pre-order  root -> left -> right
    def pre_order(self, root):
            res = []
            if root:
                res.append(root.data)
                res = res + self.pre_order(root.left)
                res = res + self.pre_order(root.right)
            
            return res

    # Post-order  left -> right -> root
    def post_order(self, root):
            res = []
            if root:
                res = self.post_order(root.left)
                res = res + self.post_order(root.right)
                res.append(root.data)
            
            return res

        
    # breadth first search
    def BFS_search(self,root,needle):
        visited = []
        queue = []
        visited.append(needle)
        queue.append(needle)

        while queue:
            m = queue.pop(0)
            print(m, end=" ")
            
            for neighbour in root.data[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return

    # depth first search
    def DFS_search(self,root,needle):
       return
               



# Driving the code
# Creating Tree
root = Node(10)
root.insert(5)
root.insert(10)
root.insert(2)
root.insert(1)
root.insert(4)
#root.print_tree()
#print(root.BST_search(root,259))
#print(root.pre_order(root))
#root.BFS_search(root,2)