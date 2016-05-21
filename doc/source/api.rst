API
===

Parse
-----

Simplify the parsing of C/C++ using libclang.  This module specifically
supports the use case of single translation units where it isn't important that
symbols from other translation units would be visible.

.. currentmodule:: glud.parsing

.. autosummary::
   parse
   parse_string 

Composition
-----------

Traverse the libclang generate AST using semantics similar to the python ast
module.

.. currentmodule:: glud.composition

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
   has_access
   has_location
   is_base_specifier
   is_class
   is_definition
   is_enum
   is_function
   is_in_file
   is_kind
   is_method
   is_namespace
   is_primitive
   is_private
   is_protected
   is_public
   is_translation_unit
   match_name
   match_typename

Higher Level Abstractions
-------------------------

Examples of the types of abstractions that it is possible to
compose with glud

.. currentmodule:: glud.higher

.. autosummary::
   is_class_definition
   superclasses
   direct_superclasses
   includes


Definitions
-----------

.. automodule:: glud.parse
   :members:

.. automodule:: glud.predicates
   :members:
   :undoc-members:

.. automodule:: glud.composition
   :members:
   :undoc-members:

.. automodule:: glud.higher
   :members:

.. automodule:: glud.dump
   :members:
