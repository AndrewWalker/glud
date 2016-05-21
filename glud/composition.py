import re
import toolz
from toolz import filter, map
import toolz.curried
import clang.cindex
from clang.cindex import *
import functools

@functools.partial
def walk(predicate, cursor):
    """Recursively yield all descendant nodes in the tree

    Find all (non-template) classes 
    """
    return filter(predicate, cursor.walk_preorder())

@toolz.curry
def iter_child_nodes(pred, cursor):
    """Yield all direct child nodes of node
    """
    return filter(pred, cursor.get_children())

@toolz.curry
def iter_predecessors(func, cursor):
    """Recursively yield all nodes based on applying a function
   
    (cursor -> cursor) -> cursor -> iter<cursor>
    """
    while cursor is not None:
        yield cursor
        cursor = func(cursor)

semantic_parents = iter_predecessors(lambda c : c.semantic_parent)

@toolz.curry
def any_fn(predicates, cursor):
    """[(cursor -> bool)] -> cursor -> bool"""
    return any(p(cursor) for p in predicates)

@toolz.curry
def all_fn(predicates, cursor):
    """[(cursor -> bool)] -> cursor -> bool"""
    return all(p(cursor) for p in predicates)

complement = toolz.curried.complement

@toolz.curry
def any_child(predicate, cursor):
    """(cursor -> bool) -> cursor -> bool"""
    it = cursor.get_children()
    return any(map(predicate, it))

@toolz.curry
def all_children(predicate, cursor):
    """(cursor -> bool) -> cursor -> bool"""
    it = cursor.get_children()
    return all(map(predicate, it))

@toolz.curry
def any_predecessor(f, predicate, cursor):
    """(cursor -> cursor) -> (cursor -> bool) -> cursor -> bool"""
    it = iter_predecessors(f, cursor)
    return any(map(predicate, it))

@toolz.curry
def all_predecessors(f, predicate, cursor):
    """(cursor -> cursor) -> (cursor -> bool) -> cursor -> bool"""
    it = iter_predecessors(f, cursor)
    return all(map(predicate, it))


