from .utils import *
from glud import ClangDiagnosticException
import io
import os

class SimpleParseTest(BaseGludTest):

    def test_bad_parse(self):
        s = '''
        void f()
        '''
        with self.assertRaises(ClangDiagnosticException) as ctx:
            c = self.parse(s)
        str(ctx.exception)

    def test_empty_file_parse(self):
        with io.open('fake.cpp','w') as fh:
            pass
        c = self.parse_file('fake.cpp')
        os.unlink('fake.cpp')
        


