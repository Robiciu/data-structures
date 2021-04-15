class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_item(self, item):
        if self.head is None:
            self.head = Node(item)
            return
        current_item = self.head
        previous_item = self.head
        if item < self.head.item:
            item = Node(item)
            item.next = self.head
            self.head = item
        else:
            while current_item:
                elem = current_item.item
                if elem > item:
                    break
                previous_item = current_item
                current_item = current_item.next
            item = Node(item)
            previous_item.next = item
            item.next = current_item

    def delete_item(self, item):
        current_item = self.head
        previous_item = self.head
        while current_item:
            elem = current_item.item
            if elem == item:
                break
            previous_item = current_item
            current_item = current_item.next
        previous_item.next = current_item.next

    def search_item(self, item):
        current_item = self.head
        while current_item:
            elem = current_item.item
            if elem == item:
                return True
            current_item = current_item.next
        return False

    def show_list(self):
        current_item = self.head
        while current_item:
            elem = current_item.item
            current_item = current_item.next
            print(elem)
