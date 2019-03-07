class Node():
    def __init__(self, key, left_child, right_child, parent):
        self.key = key
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree():
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def height(self):
        if self.tree is None:
            return 0
        return 1 + max(self.height(self.tree.left), self.height(self.tree.right))

    def size(self):
        if self.tree is None:
            return 0
        return 1 + self.size(self.tree.left) + self.size(self.tree.right)

    def depth_first_inorder_traversal(self):
        if self.tree is None:
            return
        self.depth_first_inorder_traversal(self.tree.left)
        print(self.tree.key)
        self.depth_first_inorder_traversal(self.tree.right)

    def depth_first_preorder_traversal(self):
        if self.tree is None:
            return
        print(self.tree.key)
        self.depth_first_preorder_traversal(self.tree.left)
        self.depth_first_preorder_traversal(self.tree.right)
