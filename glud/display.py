import asciitree

def dump(cursor, predicate=None):
    """Pretty print the tree of the AST represented by a cursor

    """
    if predicate is None:
        predicate = lambda c : True

    def node_children(node):
        cs = node.get_children()
        return [ c for c in cs if predicate(c) ]

    def print_node(node):
        text = node.spelling or node.displayname
        kind = str(node.kind).split('.')[1]
        return '{} {}'.format(kind, text)

    return asciitree.draw_tree(cursor, node_children, print_node)

