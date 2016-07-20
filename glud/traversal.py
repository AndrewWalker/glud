def walk(predicate, cursor):
    """Yield all nodes found by recursively visiting the AST
    """
    return (c for c in cursor.walk_preorder() if predicate(c))


def iter_child_nodes(predicate, cursor):
    """Yield all direct child nodes of node
    """
    return (c for c in cursor.get_children() if predicate(c))
