class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.item)
        if self.right:
            self.right.in_order()

    def min(self):
        if self.left:
            return self.left.min()
        return self

    def max(self):
        if self.right:
            return self.right.max()
        return self


class BST:
    def __init__(self):
        self.root = None

    def add_item(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            current = self.root
            parent = self.root
            while current:
                parent = current
                if item < current.item:
                    current = current.left
                else:
                    current = current.right
            if item < parent.item:
                parent.left = Node(item)
            else:
                parent.right = Node(item)

    def delete_item(self, item):
        if self.root.item == item:
            if self.root.left is None and self.root.right is None:
                self.root = None
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            else:
                min_right = self.root.right.min()
                left_child = self.root.left
                min_right.left = left_child
                self.root = self.root.right
        else:
            current = self.root
            parent = self.root
            while item != current.item and current:
                parent = current
                if item < current.item:
                    current = current.left
                else:
                    current = current.right
            if current.left is None and current.right is None:
                if current.item < parent.item:
                    parent.left = None
                else:
                    parent.right = None
            elif current.left and current.right is None:
                if current.item < parent.item:
                    parent.left = current.left
                else:
                    parent.right = current.left
            elif current.left is None and current.right:
                if current.item < parent.item:
                    parent.left = current.right
                else:
                    parent.right = current.right
            else:
                min_right = current.right.min()
                left_child = current.left
                min_right.left = left_child
                if current.item < parent.item:
                    parent.left = current.right
                else:
                    parent.right = current.right

    def search_item(self, item):
        if self.root is None:
            return False
        current = self.root
        while current:
            if item == current.item:
                return True
            elif item < current.item:
                current = current.left
            else:
                current = current.right
        return False

    def in_order(self):
        if self.root:
            self.root.in_order()

    def min(self):
        if self.root:
            return self.root.min().item

    def max(self):
        if self.root:
            return self.root.max().item
