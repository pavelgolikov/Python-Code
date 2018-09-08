"""DISJOINT SET FOREST + UNION BY RANK + PATH COMPRESSION."""


class Dset:
    """Disjoint set node"""

    def __init__(self, value):
        """Create an instance of Dset Node"""
        self.parent = self
        self.value = value
        self.rank = 0


def makeset(value) -> Dset:
    """Makeset operation of Disjoint Set. Creates Dset from DsetNode"""
    return Dset(value)


def find(node: Dset) -> Dset:
    """Return the head of node."""
    mem = node
    if mem.parent != mem:
        mem.parent = find(mem.parent)
    return mem.parent


def union(node1: Dset, node2: Dset) -> None:
    """Combine two dsets into one set under set1"""
    head1 = find(node1)
    head2 = find(node2)
    if head1.rank > head2.rank:
        head2.parent = head1
    elif head2.rank > head1.rank:
        head1.parent = head2
    else:
        head2.parent = head1
        head1.rank += 1


def combine_dsets(lst: list):
    """Combines Dsets into a dictionary under each representative and prints
    the dictionary.
    lst: list - list of the dset members."""
    dict_ = {}
    for el in lst:
        if find(el).value not in dict_.keys():
            dict_[find(el).value] = [el.value]
        else:
            dict_[find(el).value].append(el.value)
    return dict_
