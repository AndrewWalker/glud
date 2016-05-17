import asciitree

# This function is based on the work of Gaetan Lehmann 
# from the blog post "Playing with libclang"
# http://blog.glehmann.net/2014/12/29/Playing-with-libclang/
def dump(cursor, predicate=None):
    """Pretty print the tree of the AST represented by a cursor

    >>> tu = parse_string('void f();')
    >>> print dump(tu.cursor)
    """
    if predicate is None:
        predicate = lambda c : True

    def node_children(node):
        cs = node.get_children()
        return [ c for c in cs if predicate(c) ]

    def print_node(node):
        text = node.spelling or node.displayname
        kind = node.split(b'.')[1]
        return '{} {}'.format(kind, text)

    return asciitree.draw_tree(cursor, node_children, print_node)


