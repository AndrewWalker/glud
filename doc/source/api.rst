.. _api:

API
===

Parsing
-------

Simplify the parsing of C/C++ using libclang.  This module specifically
supports the use case of single translation units where it isn't important that
symbols from other translation units would be visible.

.. currentmodule:: glud.parsing

.. autosummary::
   parse
   parse_string 

Traversal
---------

Traverse the libclang generate AST using semantics similar to the python ast
module.

.. currentmodule:: glud.traversal

.. autosummary::
   walk
   iter_child_nodes


AST Pretty Printing
-------------------

Display the libclang AST, or a filtered subset of  

.. currentmodule:: glud.display

.. autosummary::
   dump


.. _apimatchers:

Matchers
--------

Code that implements Abstract Syntax Tree node matchers, or allow

.. currentmodule:: glud.matchers

.. autosummary::
   allOf
   anyOf
   anything
   builtinType
   classTemplateDecl
   cxxConstructorDecl
   cxxDestructorDecl
   cxxMethodDecl
   cxxRecordDecl
   decl
   enumDecl
   fieldDecl
   functionDecl
   has
   hasAncestor
   hasAnyParameter
   hasCanonicalType
   hasName
   hasParent
   hasReturnType
   hasStaticStorageDuration
   hasType
   hasTypename
   isClass
   isDefinition
   isDerivedFrom
   isExpansionInFileMatching
   isPrivate
   isProtected
   isPublic
   isSameOrDerivedFrom
   isStruct
   namespaceDecl
   parameterCountIs
   pointee
   pointerType
   recordDecl
   stmt
   typedefDecl
   unless
   varDecl


Definitions
-----------

.. automodule:: glud.parsing
   :members:
   :undoc-members:

.. automodule:: glud.traversal
   :members:

.. automodule:: glud.display
   :members:

.. automodule:: glud.matchers
   :members:
   :undoc-members:

Internal API
++++++++++++

Internal implementation details that may be useful for building new matchers,
or understanding the behavior of existing matchers. Nothing in this section is
guaranteed to remain stable between releases.


.. automodule:: glud.predicates
   :members:

.. automodule:: glud.internal
   :members:
   :undoc-members:

