class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def insert(self, root, key):
        if root is None:
            return Node(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance_factor(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
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