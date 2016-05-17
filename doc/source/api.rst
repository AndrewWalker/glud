API
===

Composition
-----------

Traverse the libclang generate AST using semantics similar to the python ast
module.

.. currentmodule:: glud.composition

.. autosummary::
   walk
   iter_child_nodes

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


Definitions
-----------

.. automodule:: glud.predicates
   :members:
   :undoc-members:

.. automodule:: glud.composition
   :members:
   :undoc-members: