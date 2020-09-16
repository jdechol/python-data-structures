class HashMap:
    def __init__(self, min_buckets=16, load_factor=.75):
        self.min_buckets = min_buckets
        self.buckets = [HashNode()] * min_buckets
        self.load_factor = load_factor
        self.size = 0

    def contains_key(self, key):
        return not self.get_node(key) is None

    def get(self, key):
        node = self.get_node(key)
        return node.value if node else None

    def get_node(self, key):
        index = calculate_hash(len(self.buckets), key)
        node = self.buckets[index]

        while node.key != key and node.next_node:
            node = node.next_node

        return node if node.key == key else None

    def put(self, key, value):
        if self.should_increase_size(key):
            self.increase_size

        node = self.get_node(key)
        if node:
            node.value = value
        else:
            index = calculate_hash(len(self.buckets), key)
            node = self.buckets[index]
            if not node.key:
                node.key = key
                node.value = value
            new_node = HashNode(key=key, value=value, next_node=node)
            self.buckets[index] = new_node

    def remove(self, key):
        if self.should_decrease_size(key):
            self.decrease_size

    def should_increase_size(self, key):
        return not self.contains_key(key) and self.size / len(self.buckets) >= self.load_factor

    def should_decrease_size(self, key):
        return self.contains_key(key) and \
               (self.size - 1) / len(self.buckets) <= self.load_factor and \
               len(self.buckets) > self.min_buckets

    def increase_size(self):
        pass

    def decrease_size(self):
        pass


def calculate_hash(num_buckets, key):
    return hash(key) % num_buckets

#
# class LinkedHashNodeList:
#     def __init__(self):



class HashNode:
    def __init__(self, key=None, value=None, next_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node
