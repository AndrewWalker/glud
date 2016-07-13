from .utils import *
from glud import *


class MatcherRegressionTest(BaseGludTest):
    """Extended tests here to verify functionaility is preserved
    """

    def test_enum_decl_aux(self):
        # Document existing behavior 

        config = '''
        namespace N {
          enum X {};
          enum class Y {};
          class Z {
           enum X {};
          };
        }'''
        spelling_names = 'N::X N::Y N::Z::X'.split()
        m = enumDecl()
        tu = parse_string(config, args='-x c++ -std=c++11'.split())
        matches = [ c.type.spelling for c in walk(m, tu.cursor) ]
        self.assertEquals( 3, len(matches) )
        self.assertEquals( 'N::X',    matches[0] )
        self.assertEquals( 'N::Y',    matches[1] )
        self.assertEquals( 'N::Z::X', matches[2] )


