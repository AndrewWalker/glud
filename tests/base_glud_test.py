import unittest2 as unittest
import ccsyspath
import glud
from glud import *

class BaseGludTest(unittest.TestCase):

    def setUp(self):
        syspath = ccsyspath.system_include_paths('clang++')
        # TODO replaced with llvm-config invocation with appropriate flags
        cargs = b'-x c++ --std=c++11 -DNDEBUG -D_GNU_SOURCE -D__STDC_CONSTANT_MACROS -D__STDC_FORMAT_MACROS -D__STDC_LIMIT_MACROS'.split()
        cargs += [ b'-I' + inc for inc in syspath ]
        self.cargs = cargs

    def parse_file(self, s, *args, **kwargs):
        kwargs['args'] = self.cargs
        return glud.parse(s, *args, **kwargs)

    def parse_tu(self, s, *args, **kwargs):
        kwargs['args'] = self.cargs
        return glud.parse_string(s, *args, **kwargs)
   
    def parse(self, s, *args, **kwargs):
        return self.parse_tu(s, *args, **kwargs).cursor




