class BinarySearchTree(object):
    """
    Represents Binary Search TNode.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_root(self):
        """
        Return the value of self.
        """
        return self.value

    def add(self, value: object) -> None:
        """Add value to BSTNode."""
        if value > self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.add(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.add(value)

    def size(self):
        """
        Return the number of elements in self.
        """
        count = 1
        if self.left:
            count += self.value.left.size()
        if self.right:
            count += self.value.right.size()
        return count

    def bin_search(self, info):
        """
        Non-recursively find whether info is in self.
        """
        try:
            if self.value == info:
                return self.value
            else:
                if info < self.value:
                    return self.left.bin_search(info)
                else:
                    return self.right.bin_search(info)
        except AttributeError:
            print('No such node found.')

    def is_empty(self):
        """
        Return whether self is empty.
        """
        return self.value is None

    def __str__(self, indent=0):
        """
        Return the string representation of self.
        """
        st = str(self.value) + '\n'
        indent += 1
        if self.right:
            st += '\t' * indent + self.right.__str__(indent)
        if self.left:
            st += '\t' * indent + self.left.__str__(indent)
        return st


class AVLNode(BinarySearchTree):
    """Represents a node for AVL tree."""

    def __init__(self, value: object) -> None:
        """Create an instance of AVL TNode."""

        BinarySearchTree.__init__(self, value)
        self.parent = None

    def insert(self, value: object) -> None:
        """Insert an item in the AVL tree."""

        # do a BST insert.
        if value > self.value:
            if self.right is None:
                new_node = AVLNode(value)
                new_node.parent = self
                self.right = new_node
                # check AVL property going up the parents
                parent = new_node.parent
                while parent is not None:
                    # print(parent)
                    if get_height(parent.left) > get_height(parent.right) + 1:
                        if get_height(parent.left.right) > \
                                get_height(parent.left.left):
                            lr(parent.left)
                        rr(parent)
                    elif get_height(parent.right) > get_height(parent.left) + 1:
                        if get_height(parent.right.left) > \
                                get_height(parent.right.right):
                            rr(parent.right)
                        lr(parent)
                    parent = parent.parent
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left is None:
                new_node = AVLNode(value)
                new_node.parent = self
                self.left = new_node
                # check AVL property going up the parents
                parent = new_node.parent
                while parent is not None:
                    # print(parent)
                    # print("height of left is", get_height(parent.left),"height of right is", get_height(parent.right))
                    if get_height(parent.left) > get_height(parent.right) + 1:
                        if get_height(parent.left.right) > \
                                get_height(parent.left.left):
                            lr(parent.left)
                        rr(parent)
                    elif get_height(parent.right) > get_height(parent.left) + 1:
                        if get_height(parent.right.left) > \
                                get_height(parent.right.right):
                            rr(parent.right)
                        lr(parent)
                    parent = parent.parent

            else:
                self.left.insert(value)


def lr(n: AVLNode) -> None:
    """Perform a left rotation of BSTNode n."""

    n.value, n.right.value = n.right.value, n.value
    right = n.right
    n.right = right.right
    right.right = right.left
    right.left = n.left
    n.left = right


def rr(n: AVLNode) -> None:
    """Perform a right rotation of BSTNode n."""

    n.value, n.left.value = n.left.value, n.value
    left = n.left
    n.left = left.left
    left.left = left.right
    left.right = n.right
    n.right = left


def get_height(node: AVLNode) -> int:
    """
    Return the height of node.
    """
    if node is None:
        return -1
    if node.left is None and node.right is None:
        return 0
    else:
        return 1 + max(get_height(node.left), get_height(node.right))


avl8 = AVLNode(8)
avl8.insert(10)
avl8.insert(3)
avl8.insert(2)
avl8.insert(1)
avl8.insert(6)
avl8.insert(4)
avl8.insert(5)
avl8.insert(7)
avl8.insert(14)
avl8.insert(13)
avl8.insert(15)
avl8.insert(16)
avl8.insert(17)
avl8.insert(9)
print(avl8)
