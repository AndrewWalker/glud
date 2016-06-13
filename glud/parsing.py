import clang.cindex
import os

__all__ = [ 'ClangDiagnosticException', 'parse_string', 'parse' ]

class ClangDiagnosticException(Exception):
    """Encapsulates Clang diagnostics as an exception
    """

    def __init__(self, diagnostic):
        self.diagnostic = diagnostic

    def __str__(self):
        s = ''
        for item in self.diagnostic:
            s += '%s\n' % item
        return s

def _ensure_parse_valid(tu):
    if len(tu.diagnostics) > 0:
        raise ClangDiagnosticException(tu.diagnostics)
    return tu        

def parse_string(contents, name='tmp.cpp', **kwargs):
    """ Parse a string of C/C++ code
    """
    idx = clang.cindex.Index.create()
    tu = idx.parse(name, unsaved_files=[(name, contents)], **kwargs)
    return _ensure_parse_valid(tu)

def parse(name, **kwargs):
    """ Parse a C/C++ file
    """
    idx = clang.cindex.Index.create()
    assert os.path.exists(name)
    tu = idx.parse(name, **kwargs)
    return _ensure_parse_valid(tu)


