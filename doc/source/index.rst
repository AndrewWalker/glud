.. highlight:: python

Glud Documentation
==================

Do you need to find something in a C++ file? Perhaps you're generating bindings
for C++ library, generating serialization code, collecting code-metrics or
developing a style checker?

You can solve all of these problems using `libclang`_, a library provided as part
of `Clang`_ compiler.  However, the challenge with libclang is that it's easy to
end up in a situation where the code you write can be difficult to write,
compose and maintain.  

Glud solves this problem by providing a higher level abstraction that makes it
easier to find C++ constructs, inspired by `libclangastmatchers`_.

Example
-------

For example, to find all of the classes in C/C++ file::

    import sys  
    import glud
    matcher = glud.isClass()
    translation_unit = glud.parse(sys.argv[1])
    for cls in glud.walk(matcher, translation_unit.cursor):
        print(cls.type.spelling)



Contents
^^^^^^^^

.. toctree::
   :maxdepth: 2

   install.rst
   quickstart.rst
   api.rst
   changelog.rst

.. _libclang: http://clang.llvm.org/doxygen/group__CINDEX.html
.. _Clang: http://clang.llvm.org/
.. _libclangastmatchers: http://clang.llvm.org/docs/LibASTMatchersReference.html
