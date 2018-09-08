"""DISJOINT SET (LINKED LIST)."""


class DsetNode:
    """Disjoint set node"""

    def __init__(self, value):
        """Create an instance of Dset Node"""
        self.set = None
        self.value = value
        self.next = None


class Dset:
    """Disjoint set node"""

    def __init__(self, node):
        """Create an instance of Disjoint Set Node. Essentially makeset."""
        self.head = node
        self.tail = node
        node.set = self


def makeset(node: DsetNode):
    """Makeset operation of Disjoint Set."""
    return Dset(node)


def find(node: DsetNode):
    """Return the head of Dset set_."""
    return node.set.head


def union(node1: DsetNode, node2: DsetNode):
    """Combine two dsets into one set under set1"""
    set1 = find(node1)
    set2 = find(node2)
    set1.set.tail.next = set2
    set1.set.tail = set2.set.tail
    mem = set2
    while mem is not None:
        mem.set = set1.set
        mem = mem.next