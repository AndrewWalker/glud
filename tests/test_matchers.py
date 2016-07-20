from .utils import *
from glud import *


class MatcherRegressionTest(BaseGludTest):
    """Extended tests here to verify functionaility is preserved
    """

    def test_func_return(self):
        config = '''
        namespace N {
          class Z {
          public:
           enum X {};
          };
          Z::X f();
        }
        '''
        tu = parse_string(config, args='-x c++ -std=c++11'.split())
        m = functionDecl(hasName('f'))
        for c in walk(m, tu.cursor):
            self.assertEquals('Z::X', c.result_type.spelling) 
            self.assertEquals('N::Z::X', c.result_type.get_canonical().spelling) 

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

    def test_anon_names(self):
        # Document existing behavior 

        config = '''
            struct X {
                enum {
                    Y = 1
                };
            };
            void f(int);
        '''
        m = hasName('Z')
        tu = parse_string(config, args='-x c++ -std=c++11'.split())
        lst = list(walk(m, tu.cursor))
            


