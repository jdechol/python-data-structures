import math


class Tree:
    def __init__(self, data=[]):
        self.data = []
        for item in data:
            self.add(item)

    def add(self, item):
        self.data.append(item)
        self.swap(0, len(self.data) - 1)
        self.bubble_up(len(self.data) - 1)
        self.bubble_down(0)

    def bubble_up(self, index: int) -> None:
        if index <= 1:
            return

        parent_index = (index - 1) // 2
        if self.data[index] % 2 == 0:  # right child
            if self.data[index] < self.data[parent_index]:
                self.swap(index, parent_index)
            self.bubble_up(parent_index)
        else:                          # left child
            if self.data[index] > self.data[parent_index]:
                self.swap(index, parent_index)
            self.bubble_up(parent_index)

    def bubble_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child <= len(self.data) - 1:
            if self.data[index] < self.data[left_child]:
                self.swap(index, left_child)
            self.bubble_down(left_child)
        if right_child <= len(self.data) - 1:
            if self.data[index] > self.data[right_child]:
                self.swap(index, right_child)
            self.bubble_down(right_child)

    def swap(self, index1, index2):
        temp = self.data[index1]
        self.data[index1] = self.data[index2]
        self.data[index2] = temp

    def remove(self, item):
        pass

    def contains(self, item) -> bool:
        return self.contains_at(item, 0)

    def contains_at(self, item, index):
        if len(self.data) == 0 or index >= len(self.data):
            return False

        if self.data[index] == item:
            return True

        child = 2 * index + 1 if item < self.data[index] else 2 * index + 2
        return self.contains_at(item, child)

    def sorted_items(self):
        pass

    def size(self):
        pass


