from typing import Any


class Stack():
    """
    Last in first out (LIFO)
    """
    def __init__(self):
        self.store = []

    def is_empty(self):
        """
        Checks whether the stack is empty
        """
        return True if not self.store else False

    def push(self, val: Any) -> None:
        """
        Adds a value to the top of the stack
        """
        self.store.append(val)

    def top(self) -> Any:
        """
        Returns the top value on the stack
        """
        if self.is_empty():
            raise Exception('Unable to top, stack is empty')
        self.store[-1]

    def pop(self) -> Any:
        """
        Returns and removes the MOST recently added key
        """
        if self.is_empty():
            raise Exception('Unable to pop, stack is empty')
        return self.store.pop()
