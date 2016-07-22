.. _quickstart:

Quickstart
==========

What is an Abstract Syntax Tree?
--------------------------------

An Abstract Syntax Tree is the data structure that a compiler converts the
source code of your program into, that is easier to work with than the bare
source code.  Python has it's own `ast module <https://docs.python.org/3/library/ast.html>`_ 
in the standard library.  

To see the what Glud knows about an AST, you can parse source, and then display
the AST.  During parsing, Glud assumes that the code you are passing it is
well-formed (would compile without errors), and will throw an exception if this
does not occur.

.. code:: 

    import sys  
    from glud import *

    translation_unit = parse(sys.argv[1])
    print(dump(translation_unit.cursor))

Which when invoked on a C++ file (tmp.cpp) that looks like this:

.. code-block:: c++

 class X {};
 struct Y {};
 class Z {
 public:
   int f(double x, char);
 };

You would expect to see an AST like:

.. code-block:: console

 TRANSLATION_UNIT tmp.cpp
   +--CLASS_DECL X
   +--STRUCT_DECL Y
   +--CLASS_DECL Z
      +--CXX_ACCESS_SPEC_DECL
      +--CXX_METHOD f
         +--PARM_DECL x
         +--PARM_DECL



Finding classes with methods
----------------------------

You can find class methods using cxxMethodDecl

.. code:: 

    import sys  
    from glud import *

    matcher = cxxRecordDecl(isClass(), has(cxxMethodDecl()))
    translation_unit = parse(sys.argv[1])
    for cls in walk(matcher, translation_unit.cursor):
        print(cls.type.spelling)


Composing Matchers
------------------

You can compose a matchers together to match more interesting criteria.  For
example, if you wanted to match methods that were public and non-static, you
could write

.. code:: 

    matcher = cxxMethodDecl(
                isPublic(),
                hasStaticStorageDuration())
    
Further Reading
---------------

Each of the matchers in the Glud API include a wide range of examples, see :ref:`apimatchers` for more information.

