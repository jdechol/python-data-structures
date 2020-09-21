from src.data.structures.trees.balanced_binary_tree import Tree


def test_contains():
    tree = Tree()
    for i in range(10):
        assert not tree.contains(i)
        tree.add(i)
        assert tree.contains(i)
