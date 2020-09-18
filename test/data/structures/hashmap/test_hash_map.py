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
        assert self.hashmap.size == 2
        self.hashmap.remove("Jared")
        assert not self.hashmap.contains_key("Jared")
        assert self.hashmap.size == 1

    def test_clear(self):
        assert self.hashmap.contains_key("Jared")
        assert self.hashmap.contains_key("John")
        self.hashmap.clear()
        assert self.hashmap.size == 0
        assert not self.hashmap.contains_key("Jared")
        assert not self.hashmap.contains_key("John")

    def test_large_size(self):
        self.hashmap.clear()
        num_range = 1000
        for i in range(num_range):
            self.hashmap.put(i, i * 2)

        assert self.hashmap.size == num_range
        for i in range(num_range):
            assert self.hashmap.get(i) == i * 2
            self.hashmap.remove(i)
            assert not self.hashmap.contains_key(i)
        assert self.hashmap.size == 0

    def test_the_thing(self):
        num_range = 100000
        maps = {}
        for i in range(num_range):
            maps[i] = i * 2

        assert len(maps) == num_range
        for i in range(num_range):
            assert maps[i] == i * 2
            maps.pop(i)
            assert not maps.get(i)
        assert len(maps) == 0
