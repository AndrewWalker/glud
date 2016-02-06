import asciitree
from toolz.functoolz import identity

def dump(cursor, func=identity):
    """Display a tree of nodes
    """

    def node_children(node):
        cs = node.get_children()
        return [ c for c in cs if func ]

    def print_node(node):
        text = node.spelling or node.displayname
        kind = str(node.kind)[str(node.kind).index('.')+1:]
        return '{} {}'.format(kind, text)

    return asciitree.draw_tree(cursor, node_children, print_node)


