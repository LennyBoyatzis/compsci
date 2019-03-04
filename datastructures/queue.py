from typing import Any


class Queue():
    """
    First come first served (FIFO)
    """
    def __init(self):
        self.store = []

    def is_empty(self):
        """
        Checks whether the stack is empty
        """
        return True if not self.store else False

    def enqueue(self, val: Any) -> None:
        """
        Adds a value to the queue
        """
        self.store.append(val)

    def dequeue(self) -> Any:
        """
        Returns and removes the LEAST recently added key
        """
        if self.is_empty():
            raise Exception('Unable to pop, queue is empty')
        return self.store.pop(0)
