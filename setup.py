from setuptools import setup, find_packages
import re
import io
import os
import sys


#def read_version():
#    with io.open('./glud/version.py', encoding='utf8') as version_file:
#        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
#        if version_match:
#            version = version_match.group(1)
#        else:
#            raise RuntimeError("Unable to find version string.")
#    return version

def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    contents = open(path).read()
    return contents

requires = [
#    'toolz',
#    'asciitree',
#    'ccsyspath',
]

if sys.version_info[1] == 2:
    requires += ['clang'] 
else: 
    requires += ['libclang-py3'] 


setup(
    name         = "glud",
    install_requires = requires,
    packages     = find_packages()
)
#    classifiers  = [
#        'Topic :: Software Development :: Compilers',
#        'Development Status :: 3 - Alpha',
#        'Intended Audience :: Developers'
#        'License :: OSI Approved :: MIT License',
#        'Natural Language :: English',
#        'Programming Language :: Python :: 2',
#        'Programming Language :: Python :: 2.6',
#        'Programming Language :: Python :: 2.7',
#        'Programming Language :: Python :: 3',
#        'Programming Language :: Python :: 3.3',
#        'Programming Language :: Python :: 3.4',
#        'Programming Language :: Python :: 3.5',
#        'Operating System :: POSIX :: Linux',
#    ]
