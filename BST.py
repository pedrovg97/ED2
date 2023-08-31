class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root
    
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)
    
    def printTree(self, root, level=0, prefix="Root: "):
        if root is not None:
            print("  " * level + prefix + str(root.key))
            self.printTree(root.left, level + 1, "L -- ")
            self.printTree(root.right, level + 1, "R -- ")