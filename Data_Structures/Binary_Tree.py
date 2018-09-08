"""BINARY TREE."""


class BTNode:
    """Binary TNode node."""

    def __init__(self, data, left=None, right=None):
        """ (BTNode, object, BTNode, BTNode) -> NoneType
        Create BTNode (self) with data and children left and right.
        """
        self.data, self.left, self.right = data, left, right

    def __str__(self, indent=0):
        """
        Return the string representation of self.
        """
        st = str(self.data) + '\n'
        indent += 1
        if self.right:
            st += '\t' * indent + self.right.__str__(indent)
        if self.left:
            st += '\t' * indent + self.left.__str__(indent)
        return st


def list_even_between(t: BTNode, start: int, stop: int) -> list:
    """ (BTNode, int, int) -> list
    Return a list of data in the tree rooted at t that
    (a) are even and (b) are between start and stop, inclusive.
    Assume that t is the value of a (possibly empty) binary
    search tree with integer elements. That is, assume:
    -- every non-empty node has integer data
    -- all data in any left sub-tree is less than the
    data in the value node
    -- all data in any right sub-tree is more than the
    data in the value node.
    """

    if t is None:
        return []
    else:
        lst = []
        if stop >= t.data >= start and t.data % 2 == 0:
            lst.append(t.data)
        if t.data >= start:
            lst += list_even_between(t.left, start, stop)
        if t.data <= stop:
            lst += list_even_between(t.right, start, stop)
        return lst


def sec_l(lst: list) -> list:
    """Return second largest element in list lst."""

    num = []
    for el in lst:
        if el is not None:
            num.append(el)
    if len(num) == 0:
        return [None, None]
    elif len(num) == 1:
        return [None, num[0]]
    elif len(num) >= 2:
        largest = max(num)
        num.remove(largest)
        second_largest1 = max(num)
        return [second_largest1, largest]


def slh(t: BTNode) -> list:
    """Helper. Returns list with first element being second largest element
    of t and second element - second largest element of t."""
    if t is None:
        return [None, None]
    else:
        left = slh(t.left)
        right = slh(t.right)
        return sec_l(left + right + [t.data])


def second_largest(t: BTNode) -> int:
    """
    Returns second largest element of t.
    """
    return slh(t)[0]


def max_value(t: BTNode) -> int:
    """Returns the maximum value in t."""
    root = t.data
    max_ = root
    if t.left:
        left_max = max_value(t.left)
        max_ = max(max_, left_max)
    if t.right:
        right_max = max_value(t.right)
        max_ = max(max_, right_max)
    return max_


def height(t):
    """
    Returns the height of t.
    """
    if t is None:
        return 0
    else:
        if not t.left and not t.right:
            return 1
        else:
            return 1 + max(height(t.left), height(t.right))


def occurs(t: BTNode, s: str) -> bool:
    """whatever"""
    if t is None or s == "":
        return t is None and s == ""
    else:
        return (s[0] == t.data) and (occurs(t.left, s[1:])
                                     or occurs(t.right, s[1:]))


def to_node_repr(lst: list, i=0) -> BTNode:
    """Given a list, return a BT representation."""
    if i >= len(lst):
        return None
    else:
        t = BTNode(lst[i])
        t.left = to_node_repr(lst, 2 * i + 1)
        t.right = to_node_repr(lst, 2 * i + 2)
        return t


def same_trees(t1, t2) -> bool:
    """Return whether t1 is same tree as t2"""
    if t1 is None or t2 is None:
        return t1 is None and t2 is None
    else:
        return t1.data == t2.data and same_trees(t1.left, t2.left) \
               and same_trees(t1.right, t2.right)


def height_(t: BTNode) -> int:
    """Return the height of t."""
    if t is None:
        return 0
    else:
        return max(height_(t.left), height_(t.right)) + 1


def num_at_level(t: BTNode, p) -> int:
    """Return the number of elements at level p"""
    if t is None:
        return 0
    elif p == 0:
        return 1
    else:
        return num_at_level(t.left, p-1) + num_at_level(t.right, p-1)


def level_nums(t: BTNode) -> list:
    """Return the list of elements at every level starting with root at
    level 0"""

    return [num_at_level(t, x) for x in range(0, height(t))]


def path_to_max(t: BTNode) -> list:
    """Return path to largest leaf."""
    if t is None:
        return []
    else:
        left = path_to_max(t.left)
        right = path_to_max(t.right)
        if left == []:
            return [t.data] + right
        elif right == []:
            return [t.data] + left
        else:
            if left[-1] >= right[-1]:
                return [t.data] + left
            else:
                return [t.data] + right


def balanced_bst(low: int, high: int) -> BTNode:
    """Return maximum balanced BTnode for values between low and high."""
    if low > high:
        return None
    else:
        root = (high - low) // 2 + low
        t = BTNode(root)
        t.left = balanced_bst(low, root - 1)
        t.right = balanced_bst(root + 1, high)
        return t


def secret_order(t: BTNode) -> list:
    """Visit nodes of t in root - right - left order."""
    if t is None:
        return []
    else:
        return [t.data] + secret_order(t.right) + secret_order(t.left)


def mutate(t, d) -> None:
    if t is None:
        pass
    else:
        mutate(t.left, d + 1)
        mutate(t.right, d + 1)
        if t.data < d:
            t.left, t.right = t.right, t.left
        else:
            t.data += d


# t1 = BTNode(2, BTNode(5, BTNode(76), BTNode(9)), BTNode(12, BTNode(8), BTNode(6)))
# t2 = BTNode(3, BTNode(4, BTNode(23)), BTNode(11, BTNode(17), BTNode(18, BTNode(10), BTNode(19))))

# t1 = BTNode(0, BTNode(2), BTNode(3))
# t2 = BTNode(1)
# t3 = BTNode(0, t1, t2)
# print(t3)
# mutate(t3, 0)
# print(t3)
# print(secret_order(t3))
# print(path_to_max(t3))