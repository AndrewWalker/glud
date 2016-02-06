====
Glud 
====

Overview
========

|license| |build| |coverage|

Glud is an abstraction on the libclang library that make matching fragments of
the clang AST simple and Pythonic, in the same way that `libclangastmatchers`_
does for the c++ clang API. 

This project is in no way affiliated with the LLVM Team or the University of
Illinois at Urbana-Champaign.


Installing
==========

Install a recent version of clang and the clang-python bindings, then install
this module as per normal.

To run glud, you'll need to make sure that libclang.so / libclang.dylib is on
your loader path.


.. _libclangastmatchers: http://clang.llvm.org/docs/LibASTMatchersReference.html

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/andrewwalker/glud/master/LICENSE
   :alt: MIT License

.. |build| image:: https://travis-ci.org/AndrewWalker/glud.svg?branch=master
   :target: https://travis-ci.org/AndrewWalker/glud
   :alt: Continuous Integration

.. |coverage| image:: https://coveralls.io/repos/github/AndrewWalker/glud/badge.svg?branch=master 
   :target: https://coveralls.io/github/AndrewWalker/glud?branch=master
   :alt: Coverage Testing Results

