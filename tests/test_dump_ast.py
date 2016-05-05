from . base_glud_test import *


class DumpAST_Tests(BaseGludTest):

    def test_dump(self):
        s = '''
        void f();
        '''
        root = self.parse(s)
        self.assertEquals(str, type(dump(root)))

    def test_empty_dump(self):
        s = ''
        root = self.parse(s)
        self.assertEquals(str, type(glud.dump(root)))


