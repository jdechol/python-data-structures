class HashMap:
    def __init__(self, min_buckets=16, load_factor=4):
        self.min_buckets = min_buckets
        self.buckets = [LinkedList() for _ in range(min_buckets)]
        self.load_factor = load_factor
        self.size = 0

    def clear(self):
        for bucket in self.buckets:
            bucket.clear()
        self.size = 0

    def contains_key(self, key):
        return self.buckets[self.get_index(key)].get(key) is not None

    def get(self, key):
        return self.buckets[self.get_index(key)].get(key)

    def put(self, key, value):
        if not self.contains_key(key):
            self.size += 1
            self.adjust_bucket_size_if_necessary()
        self.buckets[self.get_index(key)].put(key=key, value=value)

    def remove(self, key):
        index = calculate_hash(len(self.buckets), key)
        if self.buckets[index].remove(key):
            self.size -= 1
            self.adjust_bucket_size_if_necessary()

    def get_index(self, key):
        return calculate_hash(len(self.buckets), key)

    def adjust_bucket_size_if_necessary(self):
        factor = self.size / len(self.buckets)
        if factor > self.load_factor:
            self.resize_buckets(len(self.buckets) * 2)
        elif factor < (1 - self.load_factor):
            self.resize_buckets(len(self.buckets) // 2)

    def resize_buckets(self, num_buckets):
        buckets = [LinkedList() for _ in range(num_buckets)]
        for bucket in self.buckets:
            for key, value in bucket:
                buckets[calculate_hash(num_buckets, key)].put(key=key, value=value)
        self.buckets = buckets


def calculate_hash(num_buckets, key):
    return hash(key) % num_buckets


class LinkedList:
    def __init__(self, key=None, value=None):
        self.head = HashNode(key, value)
        self.tail = self.head

    def clear(self):
        self.head = HashNode()
        self.tail = self.head

    def get(self, key):
        node = self.get_node(key)
        return node.value if node and node.key == key else None

    def get_node(self, key):
        node = self.head
        while node.key != key and node.next_node:
            node = node.next_node

        return node if node.key == key else None

    def put(self, key, value):
        node = self.head
        if not node.key and node.key != 0:
            node.key = key
            node.value = value
            return

        while node.key != key and node.next_node:
            node = node.next_node

        if node.key == key:
            node.value = value
        else:
            new_node = HashNode(key=key, value=value, prev_node=self.tail)
            self.tail.next_node = new_node
            self.tail = new_node

    def remove(self, key):
        node = self.get_node(key)
        if not node:
            return False
        if node == self.head and node == self.tail:
            node.key = None
            node.value = None
        elif node == self.head:
            node.next_node.prev_node = None
            self.head = node.next_node
        elif node == self.tail:
            node.prev_node.next_node = None
            self.tail = node.prev_node
        else:
            node.prev_node.next_node = node.next_node
            node.next_node.prev_node = node.prev_node
        return True

    def __iter__(self):
        node = self.head
        while True:
            yield node.key, node.value
            if not node.next_node:
                break
            node = node.next_node


class HashNode:
    def __init__(self, key=None, value=None, next_node=None, prev_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
