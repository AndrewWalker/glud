import toolz
import collections
from .predicates import *
from .composition import *


@toolz.curry
def includes(filename, tu):
    filt = all_fn([
        is_kind(CursorKind.INCLUSION_DIRECTIVE),
        is_in_file(filename)
    ])
    return walk(filt, tu.cursor)


@toolz.curry
def direct_superclasses(predicates, cursor):
    """Yield all the recursive walk of the superclasses
    """
    filt = all_fn([is_base_specifier] + predicates)
    return ( c.get_definition() for c in iter_child_nodes(filt, cursor) )


@toolz.curry
def superclasses(predicates, cursor):
    """Yield all superclasses recursively 
    """
    f = direct_superclasses(predicates)
    Q = collections.deque()
    Q.extend(list(f(cursor)))
    while len(Q) != 0:
        c = Q.popleft()
        yield c
        Q.extend(list(f(c)))


def is_class_definition(cursor):
    return all_fn([is_class, is_definition], cursor)



