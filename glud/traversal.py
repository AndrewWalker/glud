def walk(predicate, cursor):
    """Recursively yield all descendant nodes in the tree
    Find all (non-template) classes 
    """
    return (c for c in cursor.walk_preorder() if predicate(c))

def iter_child_nodes(predicate, cursor):
    """Yield all direct child nodes of node
    """
    return (c for c in cursor.get_children() if predicate(c))
