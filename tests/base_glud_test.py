import unittest2 as unittest
import ccsyspath
import subprocess
import glud
from glud import *

class BaseGludTest(unittest.TestCase):

    def setUp(self):
        syspath = ccsyspath.system_include_paths('clang++')
        try:
            cargs = subprocess.check_output('llvm-config --cppflags') 
        except:
            # if llvm-config isn't available, guess
            cargs = '-x c++ --std=c++11'
        cargs = cargs.split()
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




