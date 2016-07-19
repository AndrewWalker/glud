Glud Documentation
==================

Glud is an abstraction on the libclang library that make matching fragments of
the Clang AST simple and Pythonic.  The intention is to produce something
that's easier to compose than the default libclang API, and is much closer to
the Clang AST Matchers library. 

Glud's priorities are:

* **Interoperability:** using glud code should not impact any
  existing libclang code, If you can't solve a problem with glud,
  you should be able to transparently fall back to using libclang
  to solve the problem.  

* **Focused on C++:** glud is heavily oriented to working with C++
  code and contains several abstractions specific to matching
  classes and member functions.


Contents
^^^^^^^^

.. toctree::
   :maxdepth: 2

   install.rst
   api.rst
   changelog.rst
