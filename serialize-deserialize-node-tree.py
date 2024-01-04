class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
class BinaryTree:
    def __init__(self):
        self.root = None
 
    # Encodes a tree to a single string.
    def serialize(self, root):
        if not root:
            return None
 
        stack = [root]
        l = []
 
        while stack:
            t = stack.pop()
 
            # If current node is NULL, store marker
            if not t:
                l.append("#")
            else:
                # Else, store current node
                # and recur for its children
                l.append(str(t.val))
                stack.append(t.right)
                stack.append(t.left)
 
        return ",".join(l)
 
    # Decodes your encoded data to tree.
    def deserialize(self, data):
        if not data:
            return None
 
        global t
        t = 0
        arr = data.split(",")
        return self.helper(arr)
 
    def helper(self, arr):
        global t
        if arr[t] == "#":
            return None
 
        # Create node with this item
        # and recur for children
        root = TreeNode(int(arr[t]))
        t += 1
        root.left = self.helper(arr)
        t += 1
        root.right = self.helper(arr)
        return root
 
    # A simple inorder traversal used
    # for testing the constructed tree
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)
 
# Driver code
if __name__ == '__main__':
    # Construct a tree shown in the above figure
    tree = BinaryTree()
    tree.root = TreeNode(20)
    tree.root.left = TreeNode(8)
    tree.root.right = TreeNode(22)
    # tree.root.left.left = TreeNode(4)
    # tree.root.left.right = TreeNode(12)
    # tree.root.left.right.left = TreeNode(10)
    # tree.root.left.right.right = TreeNode(14)
 
    serialized = tree.serialize(tree.root)
    print("Serialized view of the tree:")
    print(serialized)
    print()
 
    # Deserialize the stored tree into root1
    t = tree.deserialize(serialized)
    
    print("Inorder Traversal of the tree constructed from serialized String:")
    tree.inorder(t)