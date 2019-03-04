from datastructures.stack import Stack


def test_stack_init():
    stack = Stack()
    assert stack.store == []


def test_stack_is_empty_method():
    stack = Stack()
    assert stack.is_empty() is True
    stack.push(1)
    assert stack.is_empty() is False


def test_stack_push_method_add_value():
    stack = Stack()
    stack.push(7)
    stack.push(8)
    stack.push(9)
    assert stack.store == [7, 8, 9]


def test_stack_pop_method_returns_correct_value():
    stack = Stack()
    stack.push(7)
    stack.push(8)
    stack.push(9)
    assert stack.store == [7, 8, 9]
    stack.pop()
    assert stack.store == [7, 8]

