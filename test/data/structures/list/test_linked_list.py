from src.data.structures.list import linked_list


class TestLinkedList:
    def setup_method(self, test_method):
        self.linked_list = linked_list.LinkedList()

    def teardown_method(self, test_method):
        self.linked_list = None

    def test_add(self):
        self.linked_list.add(key="hello", value="goodbye")
        self.linked_list.add(key="john", value="smith")
        assert self.linked_list.length == 2
