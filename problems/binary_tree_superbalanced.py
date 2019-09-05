def is_balanced(tree_root) -> bool:
    """Checks to see if the difference in depth of any
    two leaf nodes is no greater than one

    Args:
        tree_root: tree root to start searching within

    Returns: bool to describe if tree is superbalanced or not
    """
    # Apply depth first search
    parent = tree_root
    difference = 0
    depth = 0

    while parent.left is not None:
        print("parent.left.value", parent.value)
        depth += 1
        parent = parent.left

    print("depth {}".format(depth))
