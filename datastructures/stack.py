from typing import Any


class Stack():
    def __init__(self):
        self.store = []

    def is_empty(self):
        return True if not self.store else False

    def push(self, val: Any) -> None:
        self.store.append(val)

    def pop(self) -> Any:
        if self.is_empty():
            raise Exception('Unable to pop, stack is empty')
        return self.store.pop()
