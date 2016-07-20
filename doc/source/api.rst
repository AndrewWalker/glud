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


Matchers
--------

Equivalents of the unstable C++ AST Matchers 

.. currentmodule:: glud.matchers

.. autosummary::
   allOf
   anyArgument
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
   isPublic
   isPrivate
   isProtected
   isSameOrDerivedFrom
   isStruct
   namespaceDecl
   parameterCountIs
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

.. automodule:: glud.predicates
   :members:
   :undoc-members:

.. automodule:: glud.matchers
   :members:
   :undoc-members:

.. automodule:: glud.traversal
   :members:
   :undoc-members:

.. automodule:: glud.display
   :members:
