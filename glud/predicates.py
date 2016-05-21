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
    """ Test if a type is a simple types (integer, boolean, char, float)
    """
    return n.kind in __primitive_types

@toolz.curry
def has_access(access, cursor):
    """ Test if a cursor has a access specifier
    See Also:
        is_public
        is_protected
        is_private
    """
    return cursor.access_specifier == access

def is_public(cursor):
    """ Test if a cursor is public
    """
    return has_access(clang.cindex.AccessSpecifier.PUBLIC, cursor)

def is_protected(cursor):
    """ Test if a cursor is protected
    """
    return has_access(clang.cindex.AccessSpecifier.PROTECTED, cursor)

def is_private(cursor):
    """ Test if a cursor is private
    """
    return has_access(clang.cindex.AccessSpecifier.PRIVATE, cursor)

@toolz.curry
def is_kind(kind, cursor):
    """ Test if a cursor or type is of a particular kind
    """
    return kind == cursor.kind

def is_function(cursor):
    """ Test if a cursor refers to a function declaration
    """ 
    return is_kind(CursorKind.FUNCTION_DECL, cursor)

def is_enum(cursor):
    """ Test if a cursor refers to an enumeration declaration
    """ 
    return is_kind(CursorKind.ENUM_DECL, cursor)

def is_class(cursor):
    """ Test if a cursor refers to a class declaration
    """ 
    return is_kind(CursorKind.CLASS_DECL, cursor)

def is_base_specifier(cursor):
    """ Test if a cursor refers to a base-declaration
    """ 
    return is_kind(CursorKind.CXX_BASE_SPECIFIER, cursor)

def is_method(cursor):
    """ Test if a cursor refers to a (non-template) member function
    """ 
    return is_kind(CursorKind.CXX_METHOD, cursor)

def is_namespace(cursor):
    """ Test if a cursor refers to a namespace
    """ 
    return is_kind(CursorKind.NAMESPACE, cursor)

def is_translation_unit(cursor):
    """ Test if a cursor refers to a translation unit

    A cursor will be a translation unit if it is the root of a parse tree
    """ 
    return is_kind(CursorKind.TRANSLATION_UNIT, cursor)

def is_definition(cursor):
    """ Test if a cursor refers to a definition

    This occurs when the cursor has a definition, and shares the location of that definiton
    """
    defn = cursor.get_definition()
    return (defn is not None) and (cursor.location == defn.location)

@toolz.curry
def match_typename(pattern, cursor):
    """ Test if the spelling of the type refered to by the cursor matches a regular expression
    """
    # this test works around a regression in libclang_py3 786b965
    typename = cursor.type.spelling
    if type(typename) is not str:
        return False
    return re.match(pattern + '$', typename) is not None

@toolz.curry
def match_name(pattern, cursor):
    """ Test if the spelling refered to by the cursor matches a regular expression
    """
    return re.match(pattern + '$', cursor.spelling) is not None

@toolz.curry
def is_in_file(files, cursor):
    """ Test if the cursor location is in a set of files
    """
    try:
        return cursor.location.file.name in files
    except:
        pass
    return False

def has_location(cursor):
    """ Test if the cursor is in a file
    """
    try:
        name = cursor.location.file.name 
        return True
    except:
        pass
    return False


