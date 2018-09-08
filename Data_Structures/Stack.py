"""STACK"""


class Stack:
    """
    Last-in, first-out (LIFO) stack.
    """

    def __init__(self) -> None:
        """
        Create a new, empty Stack self.
        """
        self._contents = []

    def add(self, obj: object) -> None:
        """
        Add object obj to top of Stack self.
        """
        self._contents.append(obj)

    def add_list(self, list_: list) -> None:
        """
        Add a list of objects to the Stack self in filo order.
        """

        for el in list_:
            self.add(el)

    def remove(self) -> object:
        """
        Remove and return top element of Stack self.
        Assume Stack self is not empty.
        """
        return self._contents.pop()

    def is_empty(self) -> bool:
        """
        Return whether Stack self is empty.
        """
        return len(self._contents) == 0