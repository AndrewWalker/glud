from setuptools import setup, find_packages
import re
import io
import os
import sys


def read_version():
    with io.open('./glud/version.py', encoding='utf8') as version_file:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
        if version_match:
            version = version_match.group(1)
        else:
            raise runtimeerror("unable to find version string.")
    return version

def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with io.open(path, encoding='utf8') as fh:
        return fh.read() 

def requires():
    if sys.version_info.major == 2:
        return ['clang'] 
    else: 
        return ['libclang-py3'] 


setup(
    name         = "glud",
    install_requires = requires(),
    description  = "Functional tools for matching nodes in the clang AST",
    long_description = read('README.rst'),
    version      = read_version(),
    author       = "Andrew Walker",
    author_email = "walker.ab@gmail.com",
    url          = "http://github.com/AndrewWalker/glud",
    license      = "MIT",
    keywords     = [ 'libclang', 'clang', 'AST' ],
    packages     = find_packages(), 
    classifiers  = [
        'Topic :: Software Development :: Compilers',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: POSIX :: Linux',
    ],
    test_suite='tests',
)
