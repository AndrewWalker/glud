from . base_glud_test import *
from clang.cindex import *
from toolz import count
from itertools import imap

class HigherOrderFuncTests(BaseGludTest):

    def test_includes(self):
        s = '''
        #include <vector>
        '''
        tu = self.parse_tu(s, options=TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD)
        incs = glud.includes('tmp.cpp', tu)
        self.assertTrue(count(incs) > 0)

    def test_is_subclassof(self):
        s = '''
        class Foo {};
        class Bar : public Foo {};
        class Baz : public Foo {};
        class Biz : public Baz {};
        class Meh {};
        class Meh2 : public Meh {};
        namespace fiz {
            class Fah : public Foo {};
            class Fal {};
        }
        '''
        def subclassof(fmatch, cursor):
            return any(imap(fmatch, superclasses([is_public], cursor)))

        root = self.parse(s)
        it = glud.walk(is_class_definition, root)
        d = {}
        for cursor in it:
            d[cursor.type.spelling] = subclassof(name_match('Foo'), cursor)
        self.assertTrue(d['Bar'])
        self.assertTrue(d['Baz'])
        self.assertTrue(d['Biz'])
        self.assertTrue(d['fiz::Fah'])
        self.assertFalse(d['Foo'])
        self.assertFalse(d['Meh'])
        self.assertFalse(d['Meh2'])
        self.assertFalse(d['fiz::Fal'])

    def test_direct_superclasses(self):
        s = '''
        class Foo {};
        class Bar : public Foo {};
        class Baz : public Bar {};
        '''
        root = self.parse(s)
        classes = glud.walk(all_fn([is_class_definition, name_match('Baz')]), root)
        classes = list(classes)
        baz = classes[0]
        baz_super = direct_superclasses([is_public], baz)
        self.assertEquals(1, len(list(baz_super)))


