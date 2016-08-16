from clang.cindex import *
from .traversal import *
import re


__all__ = [
    'Matcher', 'TrueMatcher', 'PredMatcher', 'UnlessMatcher', 'AllOfMatcher',
    'AllOfTypeMatcher', 'AnyOfMatcher', 'ChildAnyOfMatcher', 'AnyBaseClassMatcher',
    'NameMatcher', 'TypenameMatcher', 'TypeTraversalMatcher',
    'ReturnTypeTraversalMatcher', 'AnyParameterMatcher', 'AncestorMatcher',
    'LocationMatcher', 'ParentMatcher', 'ParameterMatcher',
    'ParameterCountMatcher', 'CanonicalTypeTraversalMatcher',
    'PointeeTypeTraversalMatcher', 
]


class Matcher(object):
    """Base class for matchers
    """

    def __init__(self):
        pass

    def __call__(self, cursor):
        raise NotImplemented


class TrueMatcher(Matcher):
    """Matcher that always returns true
    """

    def __init__(self):
        super(TrueMatcher, self).__init__()

    def __call__(self, cursor):
        return True


class PredMatcher(Matcher):
    def __init__(self, pred):
        super(PredMatcher, self).__init__()
        self.pred = pred

    def __call__(self, cursor):
        return self.pred(cursor)


class UnlessMatcher(Matcher):
    """Inverts the match of the children
    """

    def __init__(self, innerMatcher):
        super(UnlessMatcher, self).__init__()
        self.innerMatcher = innerMatcher

    def __call__(self, cursor):
        return not self.innerMatcher(cursor)


class AllOfMatcher(Matcher):
    """Matches if all inner matchers match
    """

    def __init__(self, *innerMatchers):
        super(AllOfMatcher, self).__init__()
        self.innerMatchers = list(innerMatchers)

    def matchNode(self, cursor):
        ms = (m(cursor) for m in self.innerMatchers)
        return all(ms)

    def __call__(self, cursor):
        return self.matchNode(cursor)


class AnyOfMatcher(Matcher):
    """Matches if any of the inner matchers match
    """

    def __init__(self, *args):
        super(AnyOfMatcher, self).__init__()
        self.matchers = list(args)

    def matchNode(self, cursor):
        ms = (m(cursor) for m in self.matchers)
        return any(ms)

    def __call__(self, cursor):
        return self.matchNode(cursor)


class ChildAnyOfMatcher(AnyOfMatcher):
    def __init__(self, *args):
        super(ChildAnyOfMatcher, self).__init__(*args)

    def children(self, cursor):
        return cursor.get_children()

    def __call__(self, cursor):
        for c in self.children(cursor):
            if self.matchNode(c):
                return True
        return False


class AnyBaseClassMatcher(AnyOfMatcher):
    def __init__(self, *args):
        super(AnyBaseClassMatcher, self).__init__(*args)

    def traverse(self, cursor):
        for c in iter_base_classes(cursor):
            yield c

    def __call__(self, cursor):
        for c in self.traverse(cursor):
            if self.matchNode(c):
                return True
        return False


class NameMatcher(Matcher):
    def __init__(self, pattern):
        super(NameMatcher, self).__init__()
        self.pattern = pattern

    def name(self, cursor):
        return cursor.spelling or ''

    def __call__(self, cursor):
        name = self.name(cursor)
        return re.match(self.pattern + '$', name) is not None


class TypenameMatcher(NameMatcher):
    def __init__(self, pattern):
        super(TypenameMatcher, self).__init__(pattern)

    def name(self, cursor):
        if cursor is None or cursor.type is None:
            return ''
        return cursor.type.spelling or ''


class AllOfTypeMatcher(AllOfMatcher):
    def __init__(self, *args):
        super(AllOfTypeMatcher, self).__init__(*args)


class TraversalMatcher(Matcher):
    def __init__(self, innerMatcher):
        super(TraversalMatcher, self).__init__()
        self.innerMatcher = innerMatcher

    def traverse(self, cursor):
        return cursor.type

    def matchNode(self, n):
        if n is None:
            return False
        return self.innerMatcher(n)

    def __call__(self, cursor):
        c = self.traverse(cursor)
        return self.matchNode(c)

class TypeTraversalMatcher(TraversalMatcher):
    def __init__(self, innerMatcher):
        super(TypeTraversalMatcher, self).__init__(innerMatcher)

    def traverse(self, cursor):
        assert(type(cursor) == Cursor), str(type(cursor))
        return cursor.type


class PointeeTypeTraversalMatcher(TraversalMatcher):
    def __init__(self, innerMatcher):
        super(PointeeTypeTraversalMatcher, self).__init__(innerMatcher)

    def traverse(self, t):
        return t.get_pointee()


class ReturnTypeTraversalMatcher(TypeTraversalMatcher):
    def __init__(self, matcher):
        super(ReturnTypeTraversalMatcher, self).__init__(matcher)

    def traverse(self, cursor):
        return cursor.result_type


class AnyParameterMatcher(Matcher):
    def __init__(self, innerMatcher):
        super(AnyParameterMatcher, self).__init__()
        self.innerMatcher = innerMatcher

    def traverse(self, cursor):
        return cursor.get_arguments()

    def matchNode(self, cursor):
        return self.innerMatcher(cursor)

    def __call__(self, cursor):
        for a in self.traverse(cursor):
            if self.matchNode(a):
                return True
        return False


class AncestorMatcher(Matcher):
    def __init__(self, innerMatcher):
        super(AncestorMatcher, self).__init__()
        self.innerMatcher = innerMatcher

    def traverse(self, cursor):
        c = cursor.semantic_parent
        while c is not None:
            yield c
            c = c.semantic_parent

    def matchNode(self, cursor):
        return self.innerMatcher(cursor)

    def __call__(self, cursor):
        for a in self.traverse(cursor):
            if self.matchNode(a):
                return True
        return False


class ParentMatcher(Matcher):
    def __init__(self, innerMatcher):
        super(ParentMatcher, self).__init__()
        self.innerMatcher = innerMatcher

    def traverse(self, cursor):
        return cursor.semantic_parent

    def matchNode(self, cursor):
        if cursor is None:
            return False
        return self.innerMatcher(cursor)

    def __call__(self, cursor):
        c = self.traverse(cursor)
        return self.matchNode(c)


class LocationMatcher(Matcher):
    def __init__(self, pattern):
        super(LocationMatcher, self).__init__()
        self.pattern = pattern

    def __call__(self, cursor):
        try:
            fname = cursor.location.file.name
            return re.match(self.pattern, fname)
        except:
            return False


class ParameterCountMatcher(Matcher):
    def __init__(self, N):
        super(ParameterCountMatcher, self).__init__()
        self.N = N

    def __call__(self, cursor):
        return self.N == len(list(cursor.get_arguments()))


class CanonicalTypeTraversalMatcher(TypeTraversalMatcher):
    def __init__(self, matcher):
        super(CanonicalTypeTraversalMatcher, self).__init__(matcher)

    def traverse(self, t):
        return t.get_canonical()


class ParameterMatcher(Matcher):
    def __init__(self, N, innerMatcher):
        super(ParameterMatcher, self).__init__()
        self.innerMatcher = innerMatcher
        self.N = N

    def matchNode(self, cursor):
        return self.innerMatcher(cursor)

    def __call__(self, cursor):
        args = list(cursor.get_arguments())
        return (len(args) > self.N) and self.matchNode(args[self.N])

