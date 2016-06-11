from .predicates import *
from .internal import *


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
