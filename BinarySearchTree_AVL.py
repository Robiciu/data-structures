class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        self.height = 0


class AVL:
    def __init__(self):
        self.root = None

    def add_item(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            self.root = self._add_item(self.root, item)

    def _add_item(self, node, item):
        if node is None:
            return Node(item)
        elif item < node.item:
            node.left = self._add_item(node.left, item)
        else:
            node.right = self._add_item(node.right, item)
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1:
            if item < node.left.item:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        if balance < -1:
            if item > node.right.item:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def delete_item(self, item):
        self.root = self._delete_item(self.root, item)

    def _delete_item(self, node, item):
        if node is None:
            return node
        elif item < node.item:
            node.left = self._delete_item(node.left, item)
        elif item < node.item:
            node.right = self._delete_item(node.right, item)
        else:
            if node.left is None:
                tmp = node.left
                node = None
                return tmp
            elif node.right is None:
                tmp = node.right
                node = None
                return tmp
            tmp = self._min(node.right)
            node.item = tmp.item
            node.right = self._delete_item(node.right, tmp.item)
        if node is None:
            return node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1:
            if self.get_balance(node.left) >= 0:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        if balance < -1:
            if self.get_balance(node.right) <= 0:
                return self.left_rotate(node)
        return node

    def search_item(self, item):
        return self._search_item(self.root, item)

    def _search_item(self, node, item):
        if node is None:
            return False
        if item == node.item:
            return True
        elif item < node.item:
            return self._search_item(node.left, item)
        elif item > node.item:
            return self._search_item(node.right, item)

    def left_rotate(self, node):
        tmp1 = node.right
        tmp2 = tmp1.left
        tmp1.left = node
        node.right = tmp2
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        tmp1.height = 1 + max(self.get_height(tmp1.left), self.get_height(tmp1.right))
        return tmp1

    def right_rotate(self, node):
        tmp1 = node.left
        tmp2 = tmp1.right
        tmp1.right = node
        node.left = tmp2
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        tmp1.height = 1 + max(self.get_height(tmp1.left), self.get_height(tmp1.right))
        return tmp1

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def min(self):
        return self._min(self.root).item

    def _min(self, node):
        if node.left:
            return self._min(node.left)
        return node

    def max(self):
        return self._max(self.root).item

    def _max(self, node):
        if node.right:
            return self._max(node.right)
        return node

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, node):
        if not node:
            return
        self._in_order(node.left)
        print(node.item)
        self._in_order(node.right)
