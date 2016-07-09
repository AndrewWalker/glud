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


Predicates
----------

Common tests for cursors and types. 

.. currentmodule:: glud.predicates

.. autosummary::
   is_builtin
   is_definition
   has_access
   is_kind
   has_storage_class
   is_decl
   is_stmt
   is_public
   is_protected
   is_private

Matchers
--------

Equivalents of the unstable C++ AST Matchers 

.. currentmodule:: glud.matchers

.. autosummary::
   allOf
   anyOf
   hasType
   anything
   anyArgument
   builtinType
   classTemplateDecl
   cxxRecordDecl
   cxxConstructorDecl
   cxxDestructorDecl
   cxxMethodDecl
   decl
   enumDecl
   fieldDecl
   functionDecl
   has
   hasName
   hasReturnType
   hasStaticStorageDuration
   hasTypename
   isDerivedFrom
   isSameOrDerivedFrom
   namespaceDecl
   recordDecl
   stmt
   typedefDecl
   unless
   isDefinition
   hasAncestor



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
