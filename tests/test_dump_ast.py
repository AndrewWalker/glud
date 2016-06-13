from .utils import *


class DumpAST_Tests(BaseGludTest):

    def test_dump(self):
        s = '''
        void f();
        '''
        root = self.parse(s)
        dmp = glud.dump(root)
        self.assertEquals(str, type(dmp))

    def test_empty_dump(self):
        s = ''
        root = self.parse(s)
        dmp = glud.dump(root)
        self.assertEquals(str, type(dmp))


