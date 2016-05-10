====
Glud 
====

Overview
========


Glud is an abstraction on the libclang library that make matching fragments of
the Clang AST simple and Pythonic, in the same way that `libclangastmatchers`_
does for the C++ Clang API. 

|license| |build| |coverage|

*Ubuntu Linux is the only offically supported target platform* 

Prerequisites
=============

Install a recent version of Clang and the python libclang bindings. On Ubuntu
you can install pre-built binaries from the llvm repositories:

.. code:: console

    wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key | sudo apt-key add -
    echo "deb http://llvm.org/apt/trusty/ llvm-toolchain-trusty-3.8 main" | sudo tee -a /etc/apt/sources.list
    sudo apt-get update -qq
    sudo apt-get install -y python-clang-3.8 libclang1-3.8

To run glud, you'll need to make sure that libclang.so is on your loader path.

.. code:: console

    sudo ln -s /usr/lib/llvm-3.8/lib/libclang-3.8.so.1 /usr/local/lib/libclang-3.8.so
    sudo ln -s /usr/lib/llvm-3.8/lib/libclang.so.1 /usr/local/lib/libclang.so
    export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

Installing
==========

You can install the latest stable version from PyPI

.. code:: console

    $ pip install glud

Or, you can install the latest development version from GitHub

.. code:: console 

    $ pip install git+git://github.com/AndrewWalker/glud.git



Acknowledgements
================

This project is in no way affiliated with the LLVM Team or the University of
Illinois at Urbana-Champaign.

Contributing
============

If you experience problems with glud, `log them on GitHub`_. If you
want to contribute code, please `fork the code`_ and `submit a pull request`_.



.. _libclangastmatchers: http://clang.llvm.org/docs/LibASTMatchersReference.html
.. _log them on Github: https://github.com/AndrewWalker/glud/issues
.. _fork the code: https://github.com/AndrewWalker/glud
.. _submit a pull request: https://github.com/AndrewWalker/glud/pulls

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/andrewwalker/glud/master/LICENSE
   :alt: MIT License

.. |build| image:: https://travis-ci.org/AndrewWalker/glud.svg?branch=master
   :target: https://travis-ci.org/AndrewWalker/glud
   :alt: Continuous Integration

.. |coverage| image:: https://coveralls.io/repos/github/AndrewWalker/glud/badge.svg?branch=master 
   :target: https://coveralls.io/github/AndrewWalker/glud?branch=master
   :alt: Coverage Testing Results

