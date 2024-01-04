# Python3 program to print 
# leaf nodes from left to right
 
# Binary tree node
class Node:
   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Function to print leaf
# nodes from left to right
def printLeafNodes(root: Node) -> None:
 
    # If node is null, return
    if (not root):
        return
 
    # If node is leaf node, 
    # print its data
    if (not root.left and
        not root.right):
        print(root.data, 
              end = " ")
        return
 
    # If left child exists, 
    # check for leaf recursively
    if root.left:
        printLeafNodes(root.left)
 
    # If right child exists, 
    # check for leaf recursively
    if root.right:
        printLeafNodes(root.right)
 
# function to find the left node and right node of parent.
def find_left_right_node(root: Node, parent: int) -> None:

     # If node is null, return
        if (not root):
            return
            
        if (root.data == parent):
                if not root.left and not root.right:
                     print("No child nodes found")

                if root.left:
                    print ("left child node is ")
                    print(root.left.data)
                if root.right:
                    print ("right child node is ")
                    print(root.right.data)
                
                return
        else:
            #Recursion
            if root.left:
                find_left_right_node(root.left,parent)

            if root.right:
                find_left_right_node(root.right,parent)
             

# Function to find parent of a node
def find_parent_of_a_node(root: Node, child: int, parent: int):
      # If node is null, return
        if (not root):
            return
        if (root.data == child):
             print("Parent of this child is "+ str(parent))
             return
        
        find_parent_of_a_node(root.left, child, root.data)
        find_parent_of_a_node(root.right, child, root.data)

 

# Driver Code
if __name__ == "__main__":
 
    # Let us create binary tree shown in
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(8)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)
 
    # print leaf nodes of the given tree
    printLeafNodes(root)
 
    # find child nodes of a parent
    find_left_right_node(root, 2)

    # find parent of a node
    find_parent_of_a_node(root, 7, -1)
