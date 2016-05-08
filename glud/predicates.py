import clang.cindex
from clang.cindex import *
import re
import toolz


__primitive_types = set([
    TypeKind.VOID,
    TypeKind.BOOL,
    TypeKind.CHAR_U,
    TypeKind.UCHAR,
    TypeKind.CHAR16,
    TypeKind.CHAR32,
    TypeKind.USHORT,
    TypeKind.UINT,
    TypeKind.ULONG,
    TypeKind.ULONGLONG,
    TypeKind.UINT128,
    TypeKind.CHAR_S,
    TypeKind.SCHAR,
    TypeKind.WCHAR,
    TypeKind.SHORT,
    TypeKind.INT,
    TypeKind.LONG,
    TypeKind.LONGLONG,
    TypeKind.INT128,
    TypeKind.FLOAT,
    TypeKind.DOUBLE,
    TypeKind.LONGDOUBLE,
    TypeKind.NULLPTR,
])

def is_primitive(n):
    return n.kind in __primitive_types

@toolz.curry
def is_kind(kind, c):
    return c.kind == kind

def has_access(access, c):
    return c.access_specifier == access

def is_func(n):
    return is_kind(CursorKind.FUNCTION_DECL, n)

def is_enum(n):
    return is_kind(CursorKind.ENUM_DECL, n)

def is_class(n):
    return is_kind(CursorKind.CLASS_DECL, n)

def is_base_specifier(n):
    return is_kind(CursorKind.CXX_BASE_SPECIFIER, n)

def is_method(n):
    return is_kind(CursorKind.CXX_METHOD, n)

def is_namespace(n):
    return is_kind(CursorKind.NAMESPACE, n)

def is_translation_unit(n):
    return is_kind(CursorKind.TRANSLATION_UNIT, n)

def is_public(c):
    return has_access(clang.cindex.AccessSpecifier.PUBLIC, c)

def is_protected(c):
    return has_access(clang.cindex.AccessSpecifier.PROTECTED, c)

def is_private(c):
    return has_access(clang.cindex.AccessSpecifier.PRIVATE, c)

def is_definition(c):
    defn = c.get_definition()
    return (defn is not None) and (c.location == defn.location)

@toolz.curry
def typename_match(pattern, cursor):
    return re.match(pattern, cursor.type.spelling)

@toolz.curry
def name_match(pattern, cursor):
    return re.match(pattern, cursor.spelling)

@toolz.curry
def is_in_file(files, c):
    try:
        return c.location.file.name in files
    except:
        pass
    return False

def has_location(c):
    try:
        name = c.location.file.name 
        return True
    except:
        pass
    return False


