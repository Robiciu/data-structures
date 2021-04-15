class Node:
    def __init__(self, item):
        self.item = item
        self.parent = None
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
            new_node = self._add_item(self.root, item)
            self._walk_up(new_node)

    def _add_item(self, node, item):
        if item < node.item:
            if node.left is None:
                node.left = Node(item)
                node.left.parent = node
                return node.left
            else:
                return self._add_item(node.left, item)
        else:
            if node.right is None:
                node.right = Node(item)
                node.right.parent = node
                return node.right
            else:
                return self._add_item(node.right, item)

    def delete_item(self, item):
        self._delete_item(item)

    def _delete_item(self, item):
        node = self._search_item(self.root, item)
        if node is not False:
            parent = self._delete_node(node)
            if parent is None and self.root:
                parent = self.root
            self._walk_up(parent)

    def _delete_node(self, node):
        parent = node.parent
        num_child = self._num_child(node)
        if num_child == 0:
            if parent is None:
                self.root = None
            elif parent.left == node:
                parent.left = None
            else:
                parent.right = None
            return parent
        elif num_child == 1:
            if node.left:
                child = node.left
            else:
                child = node.right
            if parent is None:
                self.root = child
            elif parent.left == node:
                parent.left = child
            else:
                parent.right = child
            return parent
        else:
            succesor = self._max_node(node.left)
            node.item = succesor.item
            self._delete_node(succesor)

    def _num_child(self, node):
        num_child = 0
        if node.left:
            num_child += 1
        if node.right:
            num_child += 1
        return num_child

    def _walk_up(self, node):
        if node is None:
            return
        else:
            self._check_node(node)
            return self._walk_up(node.parent)

    def _check_node(self, node):
        left_height = -1
        right_height = -1
        if node.left:
            left_height = node.left.height
        if node.right:
            right_height = node.right.height
        if abs(left_height - right_height) > 1:
            if left_height < right_height:
                self.left_rotate(node, node.right)
            else:
                self.right_rotate(node, node.left)
        else:
            node.height = max(left_height, right_height) + 1

    def search_item(self, item):
        node = self._search_item(self.root, item)
        if node is not False:
            return True
        return False

    def _search_item(self, node, item):
        if node is None:
            return False
        if item < node.item:
            return self._search_item(node.left, item)
        elif item > node.item:
            return self._search_item(node.right, item)
        return node

    def left_rotate(self, node, child):
        if child.left:
            node.right = child.left
            node.right.parent = node
        else:
            node.right = None
        if node != self.root:
            child.parent = node.parent
            node.parent.right = child
        else:
            child.parent = None
            self.root = child
        child.left = node
        node.parent = child
        node.height -= 1

    def right_rotate(self, node, child):
        if child.right:
            node.left = child.left
            node.left.parent = node
        else:
            node.left = None
        if node != self.root:
            child.parent = node.parent
            node.parent.left = child
        else:
            child.parent = None
            self.root = child
        child.right = node
        node.parent = child
        node.height -= 1

    def min(self):
        node = self._min_node(self.root)
        return node.item

    def max(self):
        node = self._max_node(self.root)
        return node.item

    def _min_node(self, node):
        if node.left:
            return self._min_node(node.left)
        return node

    def _max_node(self, node):
        if node.right:
            return self._max_node(node.right)
        return node

    def show_tree(self, method='in'):
        if method == 'in':
            self._in_order(self.root)
        elif method == 'pre':
            self._pre_order(self.root)
        elif method == 'post':
            self._post_order(self.root)

    def _in_order(self, node):
        if node.left:
            self._in_order(node.left)
        print(node.item)
        if node.right:
            self._in_order(node.right)

    def _pre_order(self, node):
        print(node.item)
        if node.left:
            self._pre_order(node.left)
        if node.right:
            self._pre_order(node.right)

    def _post_order(self, node):
        if node.left:
            self._post_order(node.left)
        if node.right:
            self._post_order(node.right)
        print(node.item)
