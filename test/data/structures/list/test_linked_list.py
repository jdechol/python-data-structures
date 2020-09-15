from src.data.structures.list.linked_list import LinkedList


class TestLinkedList:
    def setup_method(self, test_method):
        self.linked_list = LinkedList()

    def teardown_method(self, test_method):
        self.linked_list = None

    def test_add_last(self):
        assert self.linked_list.length == 0
        self.linked_list.add_last("amy")
        self.linked_list.add_last("veronica")
        assert self.linked_list.length == 2
        assert self.linked_list.contains("amy")
        assert self.linked_list.contains("veronica")
        assert not self.linked_list.contains("sally")
        assert self.linked_list.head.data == "amy"
        assert self.linked_list.tail.data == "veronica"

    def test_add_first(self):
        self.linked_list.add_first("amy")
        self.linked_list.add_first("veronica")
        assert self.linked_list.head.data == "veronica"
        assert self.linked_list.tail.data == "amy"
