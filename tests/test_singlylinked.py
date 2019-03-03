from linkedlist.singlylinked import SingleLinkedList


def test_single_linked_list_init():
    linked_list = SingleLinkedList()
    assert linked_list.head is None


def test_push_front_method():
    linked_list = SingleLinkedList()
    linked_list.push_front(7)
    assert linked_list.head is not None
