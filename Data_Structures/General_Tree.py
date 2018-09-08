"""GENERAL TREES"""


class TNode(object):
    """Represents the TNode

    Attributes:
    value - object contained in the TNode
    children - list of childern of the TNode
    """

    def __init__(self, value: object) -> None:
        """Create an instance of TNode.
        """
        self.value = value
        self.children = []

    def add(self, children: list) -> None:
        """Create an instance of TNode"""
        self.children += children

    def is_empty(self) -> bool:
        """Return whether TNode self is empty.
        """
        return self.value is None

    def __str__(self, indent=0) -> str:
        """Return a string representation of the TNode.
        """
        tot = str(self.value) + '\n'

        for child in self.children:
            tot += '\t' * (indent + 1) + child.__str__(indent + 1)
        return tot

    # def __str__(self, indent=0):
    #     """
    #     Return the string representation of self.
    #     """
    #     st = str(self.value) + '\n'
    #     indent += 1
    #     if self.right:
    #         st += '\t' * indent + self.right.__str__(indent)
    #     if self.left:
    #         st += '\t' * indent + self.left.__str__(indent)
    #     return st

    def __contains__(self, item) -> bool:
        """
        Return whether item is in TNode self.
        """
        return self.value == item or \
               any([child.__contains__(item) for child in self.children])

    def __eq__(self, other: "TNode") -> bool:
        """
        Return whether TNode t is same as TNode other.
        """

        return self.value == other.value and len(self.children) == \
               len(other.children) and \
               all((equal(self.children[i], other.children[i])
                    for i in range(len(other.children))))

    # def height(self) -> int:
    #     """
    #     Return the height of self.
    #     """
    #     max_ = 0
    #     for child in self.children:
    #         max_ = max(max_, child.height())
    #     return max_ + 1

    def height_comp(self) -> int:
        """
        Return the height of self.
        """
        return max([child.height() for child in self.children]) + 1

    def insert_root(self, value) -> None:
        """
        Insert value at the value of the TNode. Root node is added to children.
        """
        new_node = TNode(self.value)
        self.children.append(new_node)
        self.value = value

    # def equal(self, other):
    #     flag = True
    #     if self.value != other.value:
    #         return False
    #
    #     if len(self.children) == len(other.children):
    #         for i in self.children:
    #             flag = flag and self.children[i].equal(other.children[i])
    #     else:
    #         return False
    #
    #     return flag

    # def to_nested_list(self):
    #
    #     lst = []
    #     lst.append(self.value)
    #
    #     for child in self.children:
    #         lst += [child.to_nested_list()]
    #
    #     return lst

    def to_nested(self) -> list:
        """Return the list representation of this TNode
        """

        return [self.value] + [child.to_nested() for child in self.children]


    def longest_path(self):
        """Return a list of the items on the path from the value to the deepest
        leaf in the TNode. If there is a tie, pick any such leaf.
        """

        if self.is_empty():
           return []
        else:
            max_path = []
            for subnode in self.children:
               new_path = subnode.longest_path()
               if len(new_path) > len(max_path):
                   max_path = new_path
            return [self.value] + max_path


    def partition_leaves(self) -> tuple:
        """Assume TNode elements are integers.
        Return a tuple with first coordinate being the negative leaves of
        TNode self and second coordinate being the positive leaves of self.
        """
        if self is None:
            return ([], [])
        else:
            total_neg = []
            total_non_neg = []
            if self.children == []:
                # noinspection PyTypeChecker
                if self.value < 0:
                    total_neg.append(self.value)
                else:
                    total_non_neg.append(self.value)
            else:
                for child in self.children:
                    sub_tuple = child.partition_leaves()
                    total_neg += sub_tuple[0]
                    total_non_neg += sub_tuple[1]
            return (total_neg, total_non_neg)


    def truncate(self, d: int) -> None:
        """Truncate TNode below level d.
        """
        if self.is_empty():
            return
        else:
            if d == 1:
                self.value = None
                self.children = []
            elif d <= 2:
                self.children = []
            else:
                for child in self.children:
                    child.truncate(d - 1)

    def repeated_item(self, t1) -> bool:
        """"Return whether TNode t1 has repeated items."""

        if self == None:
            return False
        else:
            count = count_num_times(t1, self.value)
            print(self.value, count)
            flag = False
            if count > 1:
                return True
            for child in self.children:
                flag = flag or child.repeated_item(t1)
            return flag

    def num_at_depth(self, d: int) -> int:
        """Return the number of elements at depth d."""
        if d == 1:
            return 1
        else:
            return sum([x.num_at_depth(d - 1) for x in self.children])

    def width(self):
        """Return the width of the tree."""
        return 0 if self is None else max([self.num_at_depth(x) for x in range(1, self.height() + 1, 1)])

# def is_full (t,n):
#     """Check that TNode t is full, i.e. all nodes have either n children or
#     0.
#     """
#     flag = True
#     if t.children != []:
#         if len(t.children) != n:
#             return False
#         else:
#             for child in t.children:
#                 flag = flag and is_full(child, n)
#             return flag
#     else:
#         return True


def is_full(t: TNode, n: int) -> bool:
    """Check that TNode t is full, i.e. all nodes have either n children or 0.
    """
    return (len(t.children) == 0 or len(t.children) == n) and \
           all([is_full(child, n) for child in t.children])


def to_node(lst: list) -> TNode:
    """Return the TNode representation of Nested List lst.

    Precondition: lst has to be a valid list representation of a TNode.
    """
    t = TNode(None)
    for el in lst:
        if isinstance(el, list):
            t.children.append(to_node(el))
        else:
            t.value = el
    return t


# P = to_Node([5, [4, [3], [7], [10]], [8, [9], [6], [1]], [2]])
# print(P)


# def count_odd_above(t: TNode, n: int) -> int:
#     """
#     Return the number of odd values above level n.
#     Precondition: t's values are integers
#     """
#     if t is None:
#         return 0
#     else:
#         count = 0
#         # noinspection PyTypeChecker
#         if t.value % 2 == 1 and n > 0:
#             count += 1
#         for child in t.children:
#             count += count_odd_above(child, n - 1)
#         return count

# noinspection PyTypeChecker
def count_odd_above(t: TNode, n: int) -> int:
    """
    Return the number of odd values above level n
    Precondition: t's values are integers
    """

    return sum([count_odd_above(child, n - 1) for child in t.children]) \
               + (1 if t.value % 2 == 1 and n > 0 else 0)


# def count_even(t: TNode) -> int:
#     """
#     Count the number of even items in TNode t
#     """
#     if t == None:
#         return 0
#     else:
#         count = 0
#         if t.value % 2 == 0:
#             count += 1
#         for child in t.children:
#             count += count_even(child)
#         return count


# noinspection PyTypeChecker
def count_even(t: TNode) -> int:
    """
    Return the number of even nodes in t.
    """

    return sum([count_even(child) for child in t.children]) \
           + (1 if t.value % 2 == 0 else 0)


# def count_odd_at(t, n):
#     """
# Return the number of odd nodes of t at level n.
#     """
#
#     if t == None or n < 0:
#         return 0
#     else:
#         count = 0
#         if t.value % 2 == 1 and n == 0:
#             return 1
#         for child in t.children:
#             count += count_odd_at(child, n - 1)
#         return count

def count_odd_at(t, n):
    """
    Return the number of odd nodes of t at level n.
    """

    return sum([count_odd_at(child, n - 1) for child in t.children]) \
           + (1 if t.value % 2 == 1 and n == 0 else 0)


# def count_num_times(t: TNode, item: object) -> int:
#     """Return the number of itmes an object occurs in TNode t."""
#
#     if t is None:
#         return 0
#     else:
#         count = 0
#         if t.value == item:
#             count += 1
#         for child in t.children:
#             count += count_num_times(child, item)
#         return count

def count_num_times(t: TNode, value: object) -> int:
    """
    Return the number of times object value appears in TNode t.
    """
    return sum([count_num_times(child, value) for child in t.children]) \
           + (1 if t.value == value else 0)

# def repeated_item(t: TNode, t1: TNode) -> bool:
#     """
#     Return whether TNode t has repeated items.
#     """
#
#     if t == None:
#         return False
#     else:
#         count = count_num_times(t1, t.value)
#         flag = False
#         if count > 1:
#             return True
#         for child in t.children:
#             flag = flag or repeated_item(child, t1)
#         return flag


# def repeat_count(t: TNode) -> int:
#     """
#     Return the number of repeated items in TNode t.
#     """
#
#     def repeated_count(t: TNode, t1: TNode) -> int:
#         """
#         Helper: Return the number of items from t that appear in t1 more than
#         once.
#         Precondition: t and t1 are the same TNode.
#         """
#
#         if t is None:
#             return 0
#         else:
#             count = 0
#             item_count = count_num_times(t1, t.value)
#             if item_count > 1:
#                 count += 1
#             for child in t.children:
#                 count += repeated_count(child, t1)
#             return count
#
#     return repeated_count(t, t) // 2

def repeat_count(t: TNode) -> int:
    """
    Return the number of repeated items in TNode t.
    """

    def repeated_count(t1: TNode, t2: TNode) -> int:
        """
        Helper: Return the number of items from t that appear in t1 more than
        once.
        Precondition: t and t1 are the same TNode.
        """
        return sum([repeated_count(child, t2) for child in t1.children]) + \
               (1 if count_num_times(t2, t1.value) > 1 else 0)

    return repeated_count(t, t) // 2


# def repeated_list(t: TNode, t1: TNode, lst: list) -> list:
#     """Return the list of repeated items in TNode t."""
#
#     if t is None:
#         return []
#     else:
#         item_count = count_num_times(t1, t.value)
#         if item_count > 1 and t.value not in lst:
#             lst.append(t.value)
#
#         for child in t.children:
#             child_list = repeated_list(child, t1, lst)
#             for el in child_list:
#                 if el not in lst:
#                     lst.append(el)
#
#         return lst

def repeated_list(t1: TNode, t2: TNode, lst: list) -> list:
    """
    Return the list of repeated items in TNode t.
    """
    if count_num_times(t2, t1.value) > 1 and t1.value not in lst:
        lst.append(t1.value)
    return lst + [repeated_list(child, t2, lst) for child in t1.children]


# def count_same(t: TNode, t1: TNode) -> int:
#     """
#     Return the number of items Nodes t and t1 have in common.
#     """
#
#     if t is None or t1 is None:
#         return 0
#     else:
#         count = 0
#         item_count = count_num_times(t1, t.value)
#         if item_count > 0:
#             count += 1
#         for child in t.children:
#             count += count_same(child, t1)
#         return count

def count_same(t: TNode, t1: TNode) -> int:
    """
    Return the number of items Nodes t and t1 have in common.
    """
    return sum([count_same(child, t1) for child in t.children]) + \
           (1 if count_num_times(t1, t.value) > 0 else 0)


def list_common(t: TNode, other: TNode) -> list:
    """
    Return the list of items common to both t and other.
    """
    list_ = []
    if t.value in other:
        list_.append(t.value)
    for child in t.children:
        list_ += list_common(child, other)
    return list_


def list_common_comp(t: TNode, other: TNode) -> list:
    """
    Return the list of items common to both t and other.
    """
    return ([t.value] if t.value in other else []) \
            + sum([list_common_comp(x, other) for x in t.children], [])


def remove_root(t: TNode) -> None:
    """
    Remove the value of TNode t. Child in the left-most position becomes the value.
    Precondition: TNode has more than 1 element
    """
    if t is None:
        pass
    else:
        t.value = t.children[0].value
        remove_root(t.children[0])
        if t.children[0].children == []:
            t.children = t.children[1:]


# def remove_at_d(t: TNode, d: int) -> None:
#     """
#     Remove all nodes at height d.
#     """
#     if t is None:
#         pass
#     else:
#         if d > 0:
#             lst_to_remove = []
#             for child in t.children:
#                 if d == 1 and child.children == []:
#                     lst_to_remove.append(child)
#                 remove_at_d(child, d - 1)
#             for el in lst_to_remove:
#                 t.children.remove(el)
#         else:
#             if t.children == []:
#                 pass
#             else:
#                 t.value = t.children[0].value
#                 remove_at_d(t.children[0], d - 1)
#                 if t.children[0].children == []:
#                     t.children = t.children[1:]


def remove_at_d(t: TNode, d: int) -> None:
    """
    Remove all elements at level d of t.
    Precondition: t has more than 1 element
                  d does not exceed the height of the TNode.
    """

    if d > 1:
        for child in t.children:
            remove_at_d(child, d-1)
    elif d == 1:
        lower_children = []
        for child in t.children:
            lower_children += child.children
        t.children = lower_children
    elif d == 0:
        t.value = t.children[0].value
        t.children = t.children[1:]
        pass


def equal(t: TNode, other: TNode) -> bool:
    """
    Return whether TNode t is same as TNode other.
    """

    return t.value == other.value and len(t.children) == len(other.children) \
           and all((equal(t.children[i], other.children[i])
                    for i in range(len(other.children))))


def count_even_below(t, d: int) -> int:
    """Count the number of even elements below level d.
    """

    count = 0
    if d < 0 and t.value % 2 == 0:
        count += 1
    for child in t.children:
        count += count_even_below(child, d - 1)
    return count


def count_even_below_comp(t, d: int) -> int:
    """Count the number of even elements below level d using list comprehension.
    """

    return (1 if (d < 0 and t.value % 2 == 0) else 0) + \
           sum([count_even_below_comp(x, d - 1) for x in t.children])


def change_arity(n: TNode, d: int, list_: list) -> None:
    """Make the arity of TNode n d."""
    if n is None:
        pass
    else:
        if len(n.children) > d:
            list_ += n.children[d+1:]
            n.children = n.children[:d+1]
        elif len(n.children) < d:
            extra_nodes = list_[:(d - len(n.children)) + 1]
            list_ = list_[(d - len(n.children)) + 1:]
            n.children += extra_nodes
        index = len(list_)//len(n.children)
        total = []
        for i in range(len(n.children)):
            print(index)
            total[i] = list_[i*index:(i+1)*index]
        total[0] += list_[:index * len(n.children)]
        j = 0
        for child in n.children:
            change_arity(child, d, total[j])

# def pred (n)-> bool:
#     return n>4
#
#
# def prune (t: TNode, predicate) -> TNode:
#     if predicate(t.value) is False:
#         return None
#     else:
#         lst = [prune(x, predicate) for x in t.children]
#         t.children = [x for x in lst if x is not None]
#         return t


def unique_paths(t: TNode, s: set):
    """Check if there is a unique path from root to every node of TNode t."""
    flag = True
    # traverse the tree and put nodes in the set
    for child in t.children:
        res = unique_paths(child, s)
        flag = flag and res[0]
        for x in res[1]:
            s.add(x)
    # check if value of this tree is in the set
    if id(t) in s:
        flag = False
    # add the value to the set
    s.add(id(t))
    # return appropriate tuple
    return (flag, s)


def match_count(t: TNode) -> int:
    """Return match count for root and its children."""
    if t.children == []:
        return 0
    else:
        # find matches at this level
        curr_matches = sum([1 for x in t.children if x.value == t.value])
        children_matches = sum([match_count(child) for child in t.children])
        return curr_matches + children_matches


def preorder(t) -> None:
    """Visit nodes of t in preorder."""
    print(t.value)
    for child in t.children:
        preorder(child)


def find_odd(t: TNode):
    """Helper to find off values"""
    lst = []
    if t.value % 2 == 1:
        lst.append(t.value)
    for child in t.children:
        lst += find_odd(child)
    return lst

def odd_average(t):
    """Function to calculate the average of all odd values in TNode t."""
    odd_list = find_odd(t)
    if len(odd_list) == 0:
        return 0.0
    else:
        return sum(odd_list)/len(odd_list)

B1 = TNode(1)
B2 = TNode(2)
B3 = TNode(3)
B4 = TNode(4)
B5 = TNode(5)
B6 = TNode(6)
B7 = TNode(7)
B8 = TNode(8)
B9 = TNode(9)
B10 = TNode(10)
B11 = TNode(11)
B13 = TNode(13)
B15 = TNode(15)
B16 = TNode(16)
B22 = TNode(22)
B5.add([B4, B8, B2])
B4.add([B3, B7, B10])
B8.add([B9, B6, B11, B22])
B11.add([B13, B15, B16])
print(B5)
print(find_odd(B5))
print(odd_average(B5))
# print(preorder(B5))
# print(match_count(B5))




# B21 = TNode(1)
# B22 = TNode(21)
# B23 = TNode(31)
# B24 = TNode(41)
# B25 = TNode(51)
# B26 = TNode(61)
# B27 = TNode(71)
# B28 = TNode(8)
# B29 = TNode(9)
# B210 = TNode(10)
# B211 = TNode(111)
# B213 = TNode(13)
# B215 = TNode(15)
# B216 = TNode(161)
# B25.add([B24, B28, B22])
# B24.add([B23, B27, B210])
# B28.add([B29, B26, B211])
# B22.add([B213, B215, B216])
# print(list_common(B5, B25))
