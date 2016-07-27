from clang.cindex import *
import re


__all__ = [
    'Matcher', 'UnlessMatcher', 'AnyOfMatcher', 'ChildAnyOfMatcher',
    'AnyBaseClassMatcher', 'NameMatcher', 'TypenameMatcher', 'AllOfTypeMatcher',
    'TypeTraversalMatcher', 'ReturnTypeTraversalMatcher', 'AnyParameterMatcher',
    'AncestorMatcher', 'TrueMatcher', 'LocationMatcher', 'ParentMatcher',
    'ParameterCountMatcher', 'CanonicalTypeTraversalMatcher',
    'PointeeTypeTraversalMatcher', 'ParameterMatcher'
]


class Matcher(object):
    """Base class for matchers
    """

    def __init__(self, *args):
        self.matchers = list(args)

    def __call__(self, cursor):
        assert(cursor is not None)
        ms = (m(cursor) for m in self.matchers)
        return all(ms)


class TrueMatcher(Matcher):
    """Matcher that always returns true
    """

    def __init__(self, *args):
        super(TrueMatcher, self).__init__()

    def __call__(self, cursor):
        return True


class UnlessMatcher(Matcher):
    """Inverts the match of the children
    """

    def __init__(self, *args):
        super(UnlessMatcher, self).__init__(*args)

    def __call__(self, cursor):
        return not super(UnlessMatcher, self).__call__(cursor)


class AnyOfMatcher(Matcher):
    def __init__(self, *args):
        super(AnyOfMatcher, self).__init__(*args)

    def __call__(self, cursor):
        assert(cursor is not None)
        return any(m(cursor) for m in self.matchers)


class ChildAnyOfMatcher(AnyOfMatcher):
    def __init__(self, *args):
        super(ChildAnyOfMatcher, self).__init__(*args)

    def children(self, cursor):
        return cursor.get_children()

    def __call__(self, cursor):
        assert(cursor is not None)
        assert(type(cursor) == Cursor)
        for c in self.children(cursor):
            if super(ChildAnyOfMatcher, self).__call__(c):
                return True
        return False


class AnyBaseClassMatcher(Matcher):
    def __init__(self, *args):
        super(AnyBaseClassMatcher, self).__init__(*args)

    def __call__(self, cursor):
        assert(cursor is not None)
        assert(type(cursor) == Cursor)
        for c in cursor.get_children():
            if c.kind == CursorKind.CXX_BASE_SPECIFIER:
                cdef = c.get_definition()
                if cdef is None:
                    continue
                if any(m(cdef) for m in self.matchers):
                    return True
                elif self(cdef):
                    return True
        return False


class NameMatcher(Matcher):
    def __init__(self, pattern):
        """Test if the  name refered to by the cursor matches a regex
        """
        super(NameMatcher, self).__init__()
        self.pattern = pattern

    def __call__(self, cursor):
        name = cursor.spelling or ''
        return re.match(self.pattern + '$', name) is not None


class TypenameMatcher(Matcher):
    def __init__(self, pattern):
        """Test if the typename refered to by the cursor matches a regex
        """
        super(TypenameMatcher, self).__init__([])
        self.pattern = pattern

    def __call__(self, cursor):
        typename = cursor.type.spelling or ''
        return re.match(self.pattern + '$', typename) is not None


class AllOfTypeMatcher(object):
    def __init__(self, *args):
        self.matchers = list(args)

    def __call__(self, t):
        assert(t is not None)
        assert(type(t) == Type)
        return all(m(t) for m in self.matchers)


class TypeTraversalMatcher(object):
    def __init__(self, matcher):
        self.matcher = matcher

    def traverse(self, cursor):
        return cursor.type

    def __call__(self, cursor):
        assert(cursor is not None)
        assert(type(cursor) == Cursor)
        return self.matcher(self.traverse(cursor))


class PointeeTypeTraversalMatcher(object):
    def __init__(self, inner):
        self.inner = inner

    def __call__(self, t):
        assert(t is not None)
        assert(type(t) == Type)
        return self.inner(t.get_pointee())


class ReturnTypeTraversalMatcher(TypeTraversalMatcher):
    def __init__(self, matcher):
        super(ReturnTypeTraversalMatcher, self).__init__(matcher)

    def traverse(self, cursor):
        return cursor.result_type


class AnyParameterMatcher(object):
    def __init__(self, matcher):
        self.matcher = matcher

    def __call__(self, cursor):
        assert(cursor is not None)
        assert(type(cursor) == Cursor)
        for a in cursor.get_arguments():
            if self.matcher(a):
                return True
        return False


class AncestorMatcher(Matcher):
    def __init__(self, m):
        super(AncestorMatcher, self).__init__(m)

    def __call__(self, cursor):
        assert(cursor is not None)
        assert(type(cursor) == Cursor)
        c = cursor
        while c is not None:
            if super(AncestorMatcher, self).__call__(c):
                return True
            c = c.semantic_parent
        return False


class ParentMatcher(Matcher):
    def __init__(self, m):
        super(ParentMatcher, self).__init__(m)

    def __call__(self, cursor):
        assert(cursor is not None)
        assert(type(cursor) == Cursor)
        p = cursor.semantic_parent
        if p is None:
            return False
        return super(ParentMatcher, self).__call__(p)


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
        assert(cursor is not None)
        return self.N == len(list(cursor.get_arguments()))


class CanonicalTypeTraversalMatcher(TypeTraversalMatcher):
    def __init__(self, matcher):
        super(CanonicalTypeTraversalMatcher, self).__init__(matcher)

    def traversal(self, t):
        return t.get_canonical()

    def __call__(self, t):
        return self.matcher(self.traversal(t))


class ParameterMatcher(Matcher):
    def __init__(self, N, inner):
        super(ParameterMatcher, self).__init__(inner)
        self.N = N

    def __call__(self, cursor):
        try:
            arg = list(cursor.get_arguments())[self.N]
            return super(ParameterMatcher, self).__call__(arg)
        except:
            return False
