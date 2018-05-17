class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)

    def insert_node(self, root, data):
        if data >= root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                self.insert_node(root.right, data)
        elif data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self.insert_node(root.left, data)

    def insert(self, data):
        if self.root is None:
            self.insert_root(data)
        else:
            self.insert_node(self.root, data)

    def find_node(self, current, data):
        if current is None:
            return False
        elif current.data == data:
            return True
        elif data >= current.data:
            return self.find_node(current.right, data)
        else:
            return self.find_node(current.left, data)

    def find(self, data):
        result = self.find_node(self.root, data)
        if result is True:
            print(data, "FOUND")
        else:
            print(data, "NOT FOUND")

    def bfs(self):
        q = []
        q.append(self.root)
        while q:
            temp = q.pop(0)
            print(temp.data, end=" ")
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)

    def dfs(self):
        print("PREORDER : ", end=" ")
        self.dfs_preorder(self.root)
        print("")
        print("INORDER : ", end=" ")
        self.dfs_inorder(self.root)
        print("")
        print("POSTORDER : ", end=" ")
        self.dfs_postorder(self.root)

    def dfs_preorder(self, root):

        if root:
            print(root.data, end=" ")
            self.dfs_preorder(root.left)
            self.dfs_preorder(root.right)

    def dfs_inorder(self, root):

        if root:
            self.dfs_inorder(root.left)
            print(root.data, end=" ")
            self.dfs_inorder(root.right)

    def dfs_postorder(self, root):

        if root:
            self.dfs_postorder(root.left)
            self.dfs_postorder(root.right)
            print(root.data, end=" ")