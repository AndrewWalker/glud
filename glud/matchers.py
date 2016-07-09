from .predicates import *
from .internal import *


def allOf(*args):
    """Matches if all of the argument matchers match
    """
    return Matcher(*args)


def anyOf(*args):
    """Matches if any of the argument matchers match
    """
    return AnyOfMatcher(*args)


def hasType(matcher):
    """Matches if the type associated with the current cursor matches
    """
    return TypeTraversalMatcher(matcher)


def anything():
    """Matches anything
    """
    return TrueMatcher()


def anyArgument(matcher):
    """Match C++ class declarations 

    >>> from glud import *
    >>> config = '''
    ... void f();
    ... void g(int);
    ... '''
    >>> m = functionDecl(anyArgument(hasType(builtinType())))
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    g
    """
    return AnyArgumentMatcher(matcher)


def builtinType(*args):
    """Matches builtin primitive types (eg/ integers, booleans and float)
    """
    return AllOfTypeMatcher(is_builtin, *args)


def classTemplateDecl(*args):
    """Match C++ class declarations 

    >>> from glud import *
    >>> config = '''
    ...  template<typename T> class X {};
    ...  class Y {};
    ... '''
    >>> m = classTemplateDecl()
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    X
    """
    return Matcher(is_kind(CursorKind.CLASS_TEMPLATE), *args)


def cxxRecordDecl(*args):
    """Match C++ class declarations 

    >>> from glud import *
    >>> config = '''
    ...  class X {};
    ...  class Y {};
    ... '''
    >>> m = cxxRecordDecl()
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    X
    Y
    """
    return Matcher(is_kind(CursorKind.CLASS_DECL), *args)


def cxxConstructorDecl(*args):
    """Match C++ constructors

    >>> from glud import *
    >>> config = '''
    ...  class X {
    ...    X();
    ...  };
    ...  class Y {};
    ... '''
    >>> m = cxxConstructorDecl()
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    X
    """
    return Matcher(is_kind(CursorKind.CONSTRUCTOR), *args)


def cxxDestructorDecl(*args):
    """Match C++ destructors

    >>> from glud import *
    >>> config = '''
    ...  class X {
    ...    ~X();
    ...  };
    ...  class Y {};
    ... '''
    >>> m = cxxDestructorDecl()
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    ~X
    """
    return Matcher(is_kind(CursorKind.DESTRUCTOR), *args)
    

def cxxMethodDecl(*args):
    """Match C++ methods

    >>> from glud import *
    >>> config = '''
    ...  class X {
    ...    void u();
    ...    void v();
    ...  };
    ... '''
    >>> m = cxxMethodDecl()
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    u
    v
    """
    return Matcher(is_kind(CursorKind.CXX_METHOD), *args)


def decl(*args):
    """Match C++ methods

    >>> from glud import *
    >>> config = '''
    ...  class X {};
    ...  class Y {}; 
    ... '''
    >>> m = decl()
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    X
    Y
    """
    return Matcher(is_decl, *args)


def enumDecl(*args):
    """Match enumerations

    >>> from glud import *
    >>> config = '''
    ...  enum X {};
    ...  enum class Y {};
    ... '''
    >>> m = enumDecl()
    >>> for c in parse_string(config, args='-x c++ -std=c++11'.split()).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    X
    Y
    """
    return Matcher(is_kind(CursorKind.ENUM_DECL), *args)


def fieldDecl(*args):
    """Match struct / class fields

    >>> from glud import *
    >>> config = '''
    ...  struct X {
    ...   int u;
    ...   int v;
    ...  };
    ... '''
    >>> m = fieldDecl()
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    u
    v
    """
    return Matcher(is_kind(CursorKind.FIELD_DECL), *args)


def functionDecl(*args):
    """Match function declarations

    >>> from glud import *
    >>> config = '''
    ...  int u();
    ...  int v();
    ... '''
    >>> m = functionDecl()
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    u
    v
    """
    return Matcher(is_kind(CursorKind.FUNCTION_DECL), *args)


def has(*args):
    """Match if a cursor has a child that matches

    >>> from glud import *
    >>> config = '''
    ...  class X {
    ...   void f();
    ...  };
    ...  class Y;
    ... '''
    >>> m = cxxRecordDecl(has(cxxMethodDecl()))
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    X
    """
    return ChildAnyOfMatcher(*args)


def hasName(name):
    """Match a cursors spelling against a pattern

    >>> from glud import *
    >>> config = '''
    ...  class X {};
    ...  class Y {};
    ... '''
    >>> m = cxxRecordDecl(hasName('X'))
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    X
    """
    return NameMatcher(name)


def hasReturnType(matcher):
    """Match a function/method with a specified return type

    >>> from glud import *
    >>> config = '''
    ... class X {};
    ... X u();
    ... int v();
    ... '''
    >>> m = functionDecl(
    ...         hasReturnType(builtinType()))
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    v
    """
    return ReturnTypeTraversalMatcher(matcher)


def hasStaticStorageDuration():
    """Match an item has static storage duration

    >>> from glud import *
    >>> config = '''
    ... class X {
    ...  static void u();
    ...  void v();
    ... };
    ... '''
    >>> m = cxxMethodDecl(
    ...         hasStaticStorageDuration())
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    u
    """
    return Matcher(has_storage_class(StorageClass.STATIC))


def hasTypename(typename):
    """Match if the spelling of the type of a cursor matches a pattern

    >>> from glud import *
    >>> config = '''
    ... namespace X {
    ...  class Y {};
    ... }
    ... class Y {};
    ... '''
    >>> m = cxxRecordDecl(hasTypename('X::Y'))
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.type.spelling)
    X::Y
    """
    return TypenameMatcher(typename)


def isDerivedFrom(name):
    """Match if a C++ type inherits from a named class

    >>> from glud import *
    >>> config = '''
    ... class X {};
    ... class Y : public X {};
    ... class Z : public Y {};
    ... '''
    >>> m = cxxRecordDecl(isDerivedFrom('X'))
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    Y
    Z
    """
    return AnyBaseClassMatcher(hasTypename(name))


def isSameOrDerivedFrom(name):
    """Match if a C++ type inherits from a named class

    >>> from glud import *
    >>> config = '''
    ... class X {};
    ... class Y : public X {};
    ... class Z : public Y {};
    ... '''
    >>> m = cxxRecordDecl(isSameOrDerivedFrom('X'))
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    X
    Y
    Z
    """
    return anyOf(hasTypename(name), isDerivedFrom(name))


def namespaceDecl(*args):
    """Match a C++ namespace 

    >>> from glud import *
    >>> config = '''
    ... namespace X { }
    ... '''
    >>> m = namespaceDecl()
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    X
    """
    return Matcher(is_kind(CursorKind.NAMESPACE), *args)


def recordDecl(*args):
    """Matches structures 

    >>> from glud import *
    >>> config = '''
    ... struct X { };
    ... class Y {};
    ... '''
    >>> m = recordDecl()
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    X
    """
    return Matcher(is_kind(CursorKind.STRUCT_DECL), *args)


def stmt(*args):
    """Matches structures 

    >>> from glud import *
    >>> config = '''
    ... void f() { }
    ... '''
    >>> m = stmt()
    >>> i = 0
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         i += 1
    >>> print(i)
    1
    """
    return Matcher(is_stmt, *args)


def typedefDecl(*args):
    """Matches typedef declarations

    >>> from glud import *
    >>> config = '''
    ... typedef int X;
    ... '''
    >>> m = typedefDecl()
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    X
    """
    return Matcher(is_kind(CursorKind.TYPEDEF_DECL), *args)


def unless(*args):
    """Inverts the match of the children

    >>> from glud import *
    >>> config = '''
    ... class X { };
    ... class Y {};
    ... class Z {};
    ... '''
    >>> m = cxxRecordDecl(unless(hasName('Y')))
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    X
    Z
    """
    return UnlessMatcher(*args)


def isDefinition():
    """Inverts the match of the children

    >>> from glud import *
    >>> config = '''
    ... class X {};
    ... class Y;
    ... '''
    >>> m = cxxRecordDecl(isDefinition())
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    X
    """

    return Matcher(is_definition)


def hasAncestor(matcher):
    """Matches if the current cursor has an ancestor that matches

    >>> from glud import *
    >>> config = '''
    ... namespace X {
    ...   class Y {};
    ... }
    ... class Z {};
    ... '''
    >>> m = cxxRecordDecl(
    ...         hasName('Y'),
    ...         hasAncestor(namespaceDecl(hasName('X'))))
    >>> for c in parse_string(config).cursor.walk_preorder():
    ...     if m(c):
    ...         print(c.spelling)
    Y
    """
    return AncestorMatcher(matcher)
