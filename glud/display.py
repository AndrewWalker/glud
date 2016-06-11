try:
    from asciitree import draw_tree
except:
    from io import BytesIO

    def draw_tree(cursor, children, printer):
        def impl(node, fh, depth=0):
            fh.write('{} - {}\n'.format('  '*depth, printer(node)))
            for c in children(node):
                impl(c, fh, depth+1)

        fh = BytesIO()
        impl(cursor, fh)
        return fh.getvalue()



def dump(cursor):
    def node_children(node):
        cs = node.get_children()
        return cs

    def print_node(node):
        text = node.spelling or node.displayname
        kind = str(node.kind).split('.')[1]
        return '{} {}'.format(kind, text)

    return draw_tree(cursor, node_children, print_node)

