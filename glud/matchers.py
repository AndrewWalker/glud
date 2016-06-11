from .predicates import *
import re


class Matcher(object):
    """Base class for matchers
    """

    def __init__(self, *args):
        self.matchers = list(args)

    def __call__(self, cursor):
        assert(cursor is not None)
        ms = (m(cursor) for m in self.matchers)
        return all(ms)

    
class UnlessMatcher(Matcher):
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


class AnyBaseClassMatcher(Matcher):
    def __init__(self, *args):
        super(AnyBaseClassMatcher, self).__init__(*args)

    def __call__(self, cursor):
        assert(cursor is not None)
        assert(type(cursor) == Cursor)
        for c in cursor.get_children():
            if c.kind == CursorKind.CXX_BASE_SPECIFIER:
                cdef = c.get_definition()
                if any(m(cdef) for m in self.matchers):
                    return True
                elif self(cdef):
                    return True
        return False
    
    
class ChildAnyOfMatcher(AnyOfMatcher):
    def __init__(self, *args):
        super(ChildAnyOfMatcher, self).__init__(*args)
    
    def __call__(self, cursor):
        assert(cursor is not None)
        assert(type(cursor) == clang.cindex.Cursor)
        for c in cursor.get_children():
            if super(ChildAnyOfMatcher, self).__call__(c):
                return True
        return False

    
class NameMatcher(Matcher):
    def __init__(self, pattern):
        """Test if the  name refered to by the cursor matches a regex
        """
        super(NameMatcher, self).__init__([])
        self.pattern = pattern

    def __call__(self, cursor):
        name = cursor.spelling
        return re.match(self.pattern + '$', name) is not None


class TypenameMatcher(Matcher):
    def __init__(self, pattern):
        """Test if the typename refered to by the cursor matches a regex
        """
        super(TypenameMatcher, self).__init__([])
        self.pattern = pattern

    def __call__(self, cursor):
        typename = cursor.type.spelling
        return re.match(self.pattern + '$', typename) is not None

    
class AllOfTypeMatcher(object):
    def __init__(self, *args):
        self.matchers = list(args)

    def __call__(self, t):
        assert(t is not None)
        assert(type(t) == clang.cindex.Type)
        return all(m(t) for m in self.matchers)


class ReturnTypeTraversalMatcher(object):
    def __init__(self, matcher):
        self.matcher = matcher

    def __call__(self, cursor):
        assert(cursor is not None)
        assert(type(cursor) == clang.cindex.Cursor)
        assert(cursor.kind == CursorKind.CXX_METHOD)
        res = self.matcher(cursor.result_type)
        return res

    
class AnyArgumentMatcher(object):
    def __init__(self, matcher):
        self.matcher = matcher

    def __call__(self, cursor):
        assert(cursor is not None)
        assert(type(cursor) == clang.cindex.Cursor)
        assert(cursor.kind == CursorKind.CXX_METHOD)
        for a in cursor.get_arguments():
            if self.matcher(a):
                return True
        return False


def allOf(*args):
    return Matcher(*args)


def anyOf(*args):
    return AnyOfMatcher(*args)


def anyArgument(matcher):
    return AnyArgumentMatcher(matcher)


def builtinType(*args):
    return AllOfTypeMatcher(is_builtin, *args)


def classTemplateDecl(*args):
    return Matcher(is_kind(CursorKind.CLASS_TEMPLATE), *args)


def cxxRecordDecl(*args):
    return Matcher(is_kind(CursorKind.CLASS_DECL), *args)


def cxxConstructorDecl(*args):
    return Matcher(is_kind(CursorKind.CONSTRUCTOR), *args)


def cxxDestructorDecl(*args):
    return Matcher(is_kind(CursorKind.DESTRUCTOR), *args)
    

def cxxMethodDecl(*args):
    return Matcher(is_kind(CursorKind.CXX_METHOD), *args)


def decl(*args):
    return Matcher(is_decl, *args)


def enumDecl(*args):
    return Matcher(is_kind(CursorKind.ENUM_DECL), *args)


def fieldDecl(*args):
    return Matcher(is_kind(CursorKind.FIELD_DECL), *args)


def functionDecl(*args):
    return Matcher(is_kind(CursorKind.FUNCTION_DECL), *args)


def has(*args):
    return ChildAnyOfMatcher(*args)


def hasName(name):
    return NameMatcher(name)


def hasReturnType(matcher):
    return ReturnTypeTraversalMatcher(matcher)


def hasStaticStorageDuration():
    return Matcher(has_storage_class(StorageClass.STATIC))


def hasTypename(typename):
    return TypenameMatcher(typename)


def isDerivedFrom(name):
    return AnyBaseClassMatcher(hasTypename(name))


def isSameOrDerivedFrom(name):
    return anyOf(hasTypename(name), isDerivedFrom(name))


def namespaceDecl(*args):
    return Matcher(is_kind(CursorKind.NAMESPACE), *args)


def recordDecl(*args):
    return Matcher(is_kind(CursorKind.STRUCT_DECL), *args)


def stmt(*args):
    return Matcher(is_stmt, *args)


def typedefDecl(*args):
    return Matcher(is_kind(CursorKind.TYPEDEF_DECL), *args)


def unless(*args):
    return UnlessMatcher(*args)
