.. install::

Installation 
============

This part of the documentation covers the installation of Glud.  

Glud is a pure Python package, with minimal dependencies, but does expect that
libclang (the native code library that exposes the stable bindings to the Clang
compiler) is installed and can be dynamically loaded.  

For Python 2 development, it's also recommended that you install the Python
bindings that match your libclang, rather than relying on versions provided by
PyPI.

Prerequisites
-------------

On Ubuntu distributions, the easiest way to get an appropriate build of
libclang you can install pre-built binaries from the LLVM apt repositories.

Ubuntu Trusty (14.04)
+++++++++++++++++++++

In your terminal, enter the following commands to install libclang:

.. code:: console

    wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key | sudo apt-key add -
    echo "deb http://llvm.org/apt/trusty/ llvm-toolchain-trusty-3.8 main" | sudo tee -a /etc/apt/sources.list
    sudo apt-get update -qq
    sudo apt-get install -y python-clang-3.8 libclang1-3.8

You can then add libclang.so to your loader path, which makes the library
discoverable.

.. code:: console

    export LD_LIBRARY_PATH=/usr/lib/llvm-3.8/lib


Installation with Pip
---------------------

You can install Glud with the dependency manager pip

.. code:: console

    pip install glud


