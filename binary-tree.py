class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

    def search(self, data):
        current_node = self.root
        while current_node is not None:
            if data == current_node.data:
                return current_node
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def inorder_traversal(self, root):
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)
