class LinkedList:
    def __init__(self, data=None):
        self.length = 0
        if data:
            self.create_first_node(data)
        else:
            self.head = self.tail = None

    def add_last(self, data):
        if self.head:
            node = Node(data, prev_node=self.tail)
            self.tail.next = node
            self.tail = node
            self.length += 1
        else:
            self.create_first_node(data)

    def add_first(self, data):
        if self.head:
            node = Node(data, next_node=self.head)
            self.head.previous = node
            self.head = node
            self.length += 1
        else:
            self.create_first_node(data)

    def contains(self, key):
        return self.find_node(key) is not None

    def find_node(self, data):
        node = self.head
        while node and node.data != data:
            node = node.next

        return node if node else None

    def create_first_node(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.length = 1

class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.previous = prev_node
