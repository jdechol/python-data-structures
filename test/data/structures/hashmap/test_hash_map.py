from src.data.structures.hashmap.hash_map import HashMap


class TestHashMap:
    def setup_method(self):
        self.hashmap = HashMap()
        self.hashmap.put("Jared", "Echols")
        self.hashmap.put("John", "Doe")

    def teardown_method(self):
        self.hashmap = None

    def test_update(self):
        assert self.hashmap.get("Jared") == "Echols"
        self.hashmap.put("Jared", "Daniel")
        assert self.hashmap.get("Jared") == "Daniel"
        assert self.hashmap.get("John") == "Doe"

    def test_contains_key(self):
        assert self.hashmap.contains_key("Jared")
        assert self.hashmap.contains_key("John")

    def test_remove(self):
        pass
