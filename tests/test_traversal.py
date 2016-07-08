from .utils import *
from glud import *


class TraversalTest(BaseGludTest):

    def test_walk(self):
        s = '''
        class X {};
        class Y {};
        '''
        c = self.parse(s)
        walk(anything(), c)

    def test_iter_children(self):
        s = '''
        class X {};
        class Y {};
        '''
        c = self.parse(s)
        iter_child_nodes(anything(), c)

       


