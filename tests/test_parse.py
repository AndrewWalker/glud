from . base_glud_test import *
import os

class SimpleParseTest(BaseGludTest):

    def test_bad_parse(self):
        s = '''
        void f()
        '''
        with self.assertRaises(ClangDiagnosticException) as ctx:
            c = self.parse(s)
        str(ctx.exception)

    def test_bad_file_parse(self):
        open('fake.cpp','w').close()
        c = self.parse_file('fake.cpp')
        os.unlink('fake.cpp')
        


