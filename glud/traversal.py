from clang.cindex import *

def walk(predicate, cursor):
    """Yield all nodes found by recursively visiting the AST
    """
    return (c for c in cursor.walk_preorder() if predicate(c))


def iter_child_nodes(predicate, cursor):
    """Yield all direct child nodes of node
    """
    return (c for c in cursor.get_children() if predicate(c))


def iter_base_classes(cursor):
    for c in cursor.get_children():
        if c.kind != CursorKind.CXX_BASE_SPECIFIER:
            continue
        cdef = c.get_definition()
        if cdef is None:
            continue
        yield cdef
        for b in iter_base_classes(cdef):
            yield b
