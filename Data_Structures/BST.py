"""BST Class."""


class BinarySearchTree(object):
    """
    Represents Binary Search TNode.
    """
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def get_root(self):
        """
        Return the value of self.
        """
        return self.root

    def add(self, value: object) -> None:
        """Add value to BSTNode."""
        if value > self.root:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.add(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.add(value)

    def add_tree(self, tree: "BinarySearchTree") -> None:
        """Add BST to tree."""
        if tree.root > self.root:
            if self.right is None:
                self.right = tree
            else:
                self.right.add_tree(tree)
        else:
            if self.left is None:
                self.left = tree
            else:
                self.left.add_tree(tree)

    def size(self):
        """
        Return the number of elements in self.
        """
        count = 1
        if self.left:
            count += self.root.left.size()
        if self.right:
            count += self.root.right.size()
        return count

    def bin_search(self, info):
        """
        Non-recursively find whether info is in self.
        """
        try:
            if self.root == info:
                return self.root
            else:
                if info < self.root:
                    return self.left.bin_search(info)
                else:
                    return self.right.bin_search(info)
        except AttributeError:
            print('No such node found.')

    def is_empty(self):
        """
        Return whether self is empty.
        """
        return self.root is None

    def __str__(self, indent=0):
        """
        Return the string representation of self.
        """
        st = str(self.root) + '\n'
        indent += 1
        if self.right:
            st += '\t' * indent + self.right.__str__(indent)
        if self.left:
            st += '\t' * indent + self.left.__str__(indent)
        return st

    def num_less_than(self, i):
        """
        Return the number of elements of self that are less than i.
        """
        count = 0
        if self.root < i:
            count += 1
            if self.left is not None:
                count += self.left.num_less_than(i)
            else:
                count += 0
            if self.right is not None:
                count += self.right.num_less_than(i)
            else:
                count += 0
        else:
            if self.left is not None:
                count += self.left.num_less_than(i)
            else:
                count += 0
        return count

    #    def num_less_than(self, i):
    #        count = 0
    #        print(self.value)
    #        if self.value < i:
    #            count += 1
    #            try:
    #                count += self.left.num_less_than(i)
    #            except AttributeError:
    #                count+=0
    #            try:
    #                count += self.right.num_less_than(i)
    #            except AttributeError:
    #                count+=0
    #
    #        else:
    #            count+=0
    #            try:
    #                count += self.left.num_less_than(i)
    #            except AttributeError:
    #                count+=0
    #
    #        return count

    def items_at_depth(self, d):
        """
        Return elements of self at level d.
        """
        lst = []
        if d == 1:
            lst.append(self.root)

        try:
            lst += self.left.items_at_depth(d - 1)
        except AttributeError:
            lst += []
        try:
            lst += self.right.items_at_depth(d - 1)
        except AttributeError:
            lst += []
        return lst

    def height(self):
        """
        Return the height of tree self.
        """
        try:
            height_left = self.left.height()
        except AttributeError:
            height_left = 0
        try:
            height_right = self.right.height()
        except AttributeError:
            height_right = 0

        h = max(height_left, height_right) + 1
        return h

    def level(self):
        """
        Return levels of self.
        """
        lst = []
        for h in range(self.height()):
            lst += [(h + 1, self.items_at_depth(h + 1))]
        return lst

    def contains(self, item):
        """
        Return whether self contains item.
        """
        if self.root == item:
            return True
        if item < self.root:
            if self.left is not None:
                return self.left.contains(item)
            else:
                return False

        else:
            if self.right is not None:
                return self.right.contains(item)
            else:
                return False

    def s_l_h(self, level: int):
        """Return the second largest element of self."""
        if self.root is None:
            return 0
        elif level == 1:
            left = self.left.s_l_h(level + 1)
            right = self.right.s_l_h(level + 1)
            if left >= right and self.root >= right:
                return min(left, self.root)
            elif right >= left and self.root >= left:
                return min(left, self.root)
            elif right >= self.root and left >= self.root:
                return min(left, right)
        else:
            left = self.left.s_l_h(level + 1)
            right = self.right.s_l_h(level + 1)
            return max(left, right, self.root)

    def levels(self) -> list:
        """Return tuples corresponding to levels."""
        if self.root is None:
            return [(1, [])]
        else:
            left, right = [], []
            if self.left is not None:
                left = self.left.levels()
            if self.right is not None:
                right = self.right.levels()
            total = [(1, [self.root])]
            new_left = [(x[0] + 1, x[1]) for x in left]
            new_right = [(y[0] + 1, y[1]) for y in right]
            com = None
            if len(new_left) > len(new_right):
                com = [(new_left[x][0], new_left[x][1] + new_right[x][1]) for x
                       in range(len(new_right))]
                com.append(new_left[len(new_right)])
            if len(new_left) < len(new_right):
                com = [(new_left[x][0], new_left[x][1] + new_right[x][1]) for x
                       in range(len(new_left))]
                com.append(new_right[len(new_left)])
            if len(new_left) == len(new_right):
                com = [(new_left[x][0], new_left[x][1] + new_right[x][1]) for x
                       in range(len(new_left))]
            total += com
            return total


def is_bst(t: BinarySearchTree) -> bool:
    """
    Return True if and only if t is a BST.
    """
    if t is None:
        return True
    else:
        flag = True
        if t.left is not None:
            flag = flag and (t.left.root <= t.root) and (is_bst(t.left))
        if t.right is not None:
            flag = flag and (t.root < t.right.root) and (is_bst(t.right))
        return flag


def size(t: BinarySearchTree) -> int:
    """
    Return the size of this BST.
    """
    if not t:
        return 0
    else:
        return 1 + size(t.left) + size(t.right)


def num_leaves(t: BinarySearchTree) -> int:
    """
    Return the number of leaves of t.
    """
    if not t:
        return 0
    else:
        if not t.left and not t.right:
            return 1
        else:
            return num_leaves(t.left) + num_leaves(t.right)


def list_internal(t: BinarySearchTree) -> list:
    """Return the list of leaves of t"""
    if not t or (not t.left and not t.right):
        return []
    else:
        return [t.root] + list_internal(t.left) + list_internal(t.right)


def times(t: BinarySearchTree, item: object) -> int:
    """Return the number of times an item is in a tree t."""
    if not t:
        return 0
    else:
        count = 0
        if t.root == item:
            count += 1
        return count + times(t.left, item) + times(t.right, item)


def max_item(t: BinarySearchTree) -> int:
    """Return the maximum value in the tree t"""
    if not t:
        raise ValueError("Empty TNode")
    else:
        if not t.right:
            return t.root
        else:
            return max_item(t.right)


def k_th(t: BinarySearchTree, k: int) -> int:
    """Return the k'th smallest item in BST t. k - int > 0"""
    if not t:
        pass
    else:
        if size(t.left) == k - 1:
            return t.root
        elif size(t.left) >= k:
            return k_th(t.left, k)
        elif size(t.left) < k:
            return k_th(t.right, k - (size(t.left) + 1))


def le_k(t: BinarySearchTree, k: int) -> list:
    """Return the list of items of t that are less than or equal to k."""
    if not t:
        return []
    else:
        if t.root == k:
            return [t.root] + le_k(t.left, k)
        elif t.root < k:
            return [t.root] + le_k(t.left, k) + le_k(t.right, k)
        elif t.root > k:
            return le_k(t.left, k)


def ge_k(t: BinarySearchTree, k: int) -> list:
    """Return the list of items if t that are greater than of equal to k"""
    if not t:
        return []
    else:
        if t.root == k:
            return [t.root] + ge_k(t.right, k) + ge_k(t.left, k)
        elif t.root < k:
            return ge_k(t.right, k)
        elif t.root > k:
            return [t.root] + ge_k(t.left, k) + ge_k(t.right, k)


def remover(t: BinarySearchTree, it: object) -> BinarySearchTree:
    """Return tree t with it removed from it."""
    if not t:
        pass
    else:
        if t.root == it:
            if not t.left and t.right:
                return t.right
            elif t.left and not t.right:
                return t.left
            elif not t.right and not t.left:
                pass
            elif t.left and t.right:
                repl = t.right
                while repl.left:
                    repl = repl.left
                t.root = repl.root
                t.right = remover(t.right, repl.root)
                return t
        else:
            if it > t.root:
                t.right = remover(t.right, it)
                return t
            elif it < t.root:
                t.left = remover(t.left, it)
                return t


def remove_all(t: BinarySearchTree, it: object) -> BinarySearchTree:
    """Remove all occurences of object it from  BST t. If doesn't work,
    replace passes with return None."""

    if not t:
        pass
    else:
        if t.root == it:
            if not t.left and not t.right:
                pass
            elif t.left and not t.right:
                t.left = remove_all(t.left, it)
                return t.left
            elif t.right and not t.left:
                t.left = remove_all(t.left, it)
                return t.right
            elif t.right and t.left:
                repl = t.right
                while repl.left:
                    repl = repl.left
                t.root, repl.root = repl.root, t.root
                t.right = remove_all(t.right, it)
                t.left = remove_all(t.left, it)
                return t
        else:
            if it < t.root:
                t.left = remove_all(t.left, it)
                return t
            elif it > t.root:
                t.right = remove_all(t.right, it)
                return t


def remove_under_d(t: BinarySearchTree, d: int) -> BinarySearchTree:
    """Remove all nodes with values less than d from BST t."""

    if not t:
        pass
    else:
        if t.root == d:
            return t.right
        elif t.root > d:
            t.left = remove_under_d(t.left, d)
            return t
        elif t.root < d:
            return remove_under_d(t.right, d)


def remove_all_even(t: BinarySearchTree) -> BinarySearchTree:
    """Remove all even elements of BST t."""

    if not t:
        pass
    else:
        if t.root % 2 == 1:
            t.right = remove_all_even(t.right)
            t.left = remove_all_even(t.left)
            return t
        else:
            if not t.left and not t.right:
                pass
            elif not t.left and t.right:
                return remove_all_even(t.right)
            elif t.left and not t.right:
                return remove_all_even(t.left)
            elif t.left and t.right:
                t.left = remove_all_even(t.left)
                t.right = remove_all_even(t.right)
                rep = t.right
                prev = t.right
                while rep.left:
                    prev = rep
                    rep = rep.left
                if rep == prev:
                    t.root = rep.root
                    t.right = rep.right
                else:
                    t.root = rep.root
                    prev.left = rep.right
                return t


def copy_tree(t: BinarySearchTree) -> BinarySearchTree:
    """Return the copy of t."""
    if t is None:
        pass
    else:
        new = BinarySearchTree(t.root)
        # if t.left is not None:
        new.left = copy_tree(t.left)
        # if t.right is not None:
        new.right = copy_tree(t.right)
        return new


def restructure(t, value, list_) -> BinarySearchTree:
    """Return a new tree with value as a root."""
    if t.root == value:
        new_tree = copy_tree(t)
        for subtree in list_:
            new_tree.add_tree(subtree)
        return new_tree
    elif value > t.root:
        # going right
        new_left = copy_tree(t.left)
        new_tree = BinarySearchTree(t.root)
        new_tree.left = new_left
        list_.append(new_tree)
        return restructure(t.right, value, list_)
    elif value < t.root:
        # going left
        new_right = copy_tree(t.right)
        new_tree = BinarySearchTree(t.root)
        new_tree.right = new_right
        list_.append(new_tree)
        return restructure(t.left, value, list_)


def restructure_alt(t, value, list_) -> BinarySearchTree:
    """Return a new tree with value as a root."""
    if t.root == value:
        for subtree in list_:
            t.add_tree(subtree)
        return t
    elif value > t.root:
        # going right
        right = t.right
        t.right = None
        list_.append(t)
        return restructure_alt(right, value, list_)
    elif value < t.root:
        # going left
        left = t.left
        t.left = None
        list_.append(t)
        return restructure_alt(left, value, list_)


def has_path_sum(t: BinarySearchTree, total: int) -> bool:
    """Return whether t has a path with sum total along it."""

    if total == 0 or t is None:
        return total == 0 and t is None
    else:
        return has_path_sum(t.left, total - t.root) \
               or has_path_sum(t.right, total - t.root)


def find_left_streak(t: BinarySearchTree) -> BinarySearchTree:
    """Find the shallowest subtree with the left streak."""
    if t is None:
        pass
    else:
        streak_parent = t
        while streak_parent.left is not None:
            node = streak_parent.left
            if (node.left is not None and node.right is None) and \
                    (node.left.left is not None and node.left.right is None):
                return streak_parent
            streak_parent = node


def fix_streaks(t: BinarySearchTree) -> None:
    """Fix all left streaks in t"""
    if find_left_streak(t) is None:
        pass
    else:
        if find_left_streak(t) == t:
            new_bst = BinarySearchTree(t.root)
            t.root = t.left.root
            t.right = new_bst
            t.left = t.left.left

        fix_streaks(t.left)
        fix_streaks(t.right)


# B8 = BinarySearchTree(8)
# B8.add(10)
# B8.add(3)
# B8.add(2)
# B8.add(1)
# B8.add(6)
# B8.add(4)
# B8.add(5)
# B8.add(7)
# B8.add(14)
# B8.add(13)
# B8.add(15)
# B8.add(9)
# print(B8)
# print(find_left_streak(B8))
# fix_streaks(B8)
# print(B8)

# print(has_path_sum(B8, 13))
# B8 = restructure_alt(B8, 6, [])
# print(B8)
# print(is_bst(B8))
# B8 = restructure_alt(B8, 9, [])
# print(B8)
# print(is_bst(B8))

# B88 = BSTNode(8)
# B88.add(3)
# B88.add(10)
# B88.add(1)
# B88.add(6)
# B88.add(4)
# B88.add(5)
# B88.add(7)
# B88.add(14)
# B88.add(13)

# print (B8.to_nested_list())

# print(B8.equal(B88))

# print(B8.contains(0))
# print(B8.level())
# print(B8.items_at_depth(3))
# print(B8.num_less_than(6))
