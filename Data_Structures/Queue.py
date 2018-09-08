"""QUEUE"""


class Queue:
    """
    A first-in, first-out (FIFO) queue.
    """

    def __init__(self) -> None:
        """
        Create and initialize new Queue self.
        """
        self._contents = []

    def __str__(self) -> str:
        """
        Return a string representation of Queue self.
        """

        return str(self._contents)

    def __eq__(self, other: 'Queue') -> bool:
        """
        Return whether this Queue is the same as other Queue.
        """
        return type(self) == type(other) and self._contents == other._contents

    def add(self, obj: object) -> None:
        """
        Add object at the back of Queue self.
        """
        self._contents.append(obj)

    def remove(self) -> object:
        """
        Remove and return front object from Queue self.
        Queue self must not be empty.
        """
        return self._contents.pop(0)

    def is_empty(self) -> bool:
        """
        Return whether Queue self is empty
        """
        return len(self._contents) == 0