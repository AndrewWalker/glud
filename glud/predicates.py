from clang.cindex import AccessSpecifier, StorageClass
from clang.cindex import *

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


def is_builtin(n):
    """ Test if a type is a simple types (integer, boolean, char, float)
    """
    return n.kind in __primitive_types


def is_definition(cursor):
    """Test if a cursor refers to a definition

    This occurs when the cursor has a definition, and shares the location of that definiton
    """
    defn = cursor.get_definition()
    return (defn is not None) and (cursor.location == defn.location)

def has_access(access):
    """ Test if a cursor has a access specifier
    """
    def _has_access(cursor):
        return cursor.access_specifier == access
    return _has_access


def is_kind(kind):
    """ Test if a cursor or type is of a particular kind
    """
    def _is_kind(cursor):
        return kind == cursor.kind
    return _is_kind


def has_storage_class(kind):
    """Check if the cursor has a particular (eg/ static) storage class
    """
    def _has_storage_class(cursor):
        return cursor.storage_class == kind
    return _has_storage_class


def is_decl(c):
    """Check if a cursor is a declaration
    """
    return c.kind.is_declaration()


def is_stmt(c):
    """Check if a cursor is a statement
    """
    return c.kind.is_declaration()


is_public = has_access(AccessSpecifier.PUBLIC)
is_public.__doc__ = 'Test if a cursor is public'

is_protected = has_access(AccessSpecifier.PROTECTED)
is_protected.__doc__ = 'Test if a cursor is protected'

is_private = has_access(AccessSpecifier.PRIVATE)
is_private.__doc__ = 'Test if a cursor is private'


