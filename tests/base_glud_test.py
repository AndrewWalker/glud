import unittest2 as unittest
import os
import yaml
import toolz
from itertools import imap

import clang.cindex
#clang.cindex.conf.set_library_file('/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/libclang.dylib')
from clang.cindex import *

import glud
from glud import *


class BaseGludTest(unittest.TestCase):
    def setUp(self):
        d = yaml.load(open(os.path.expanduser('~/.gludrc'),'r'))
        cargs = ['-I' + inc for inc in d['syspath']]
        cargs+= d['args'].split()

        def _parse_file(s, *args, **kwargs):
            kwargs['args'] = cargs
            return glud.parse(s, *args, **kwargs)
 
        def _parse_tu(s, *args, **kwargs):
            kwargs['args'] = cargs
            return glud.parse_string(s, *args, **kwargs)
       
        def _parse(s, *args, **kwargs):
            return _parse_tu(s, *args, **kwargs).cursor

        self._parse = _parse
        self._parse_file = _parse_file
        self._parse_tu = _parse_tu



