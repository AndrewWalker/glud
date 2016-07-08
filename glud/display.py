from asciitree import draw_tree


def dump(cursor):
    def node_children(node):
        return list(node.get_children())

    def print_node(node):
        text = node.spelling or node.displayname
        kind = str(node.kind).split('.')[1]
        return '{} {}'.format(kind, text)

    return draw_tree(cursor, node_children, print_node)

