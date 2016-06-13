import unittest
import glud


def count(iterable):
    return sum(1 for _ in iterable)


class BaseGludTest(unittest.TestCase):

    def setUp(self):
        cargs = '-x c++ --std=c++11'
        cargs = cargs.split()
        self.cargs = cargs

    def parse_file(self, s, *args, **kwargs):
        kwargs['args'] = self.cargs
        return glud.parse(s, *args, **kwargs)

    def parse_tu(self, s, *args, **kwargs):
        kwargs['args'] = self.cargs
        return glud.parse_string(s, *args, **kwargs)
   
    def parse(self, s, *args, **kwargs):
        return self.parse_tu(s, *args, **kwargs).cursor




