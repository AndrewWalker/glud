from . base_glud_test import *
from clang.cindex import *
from toolz import count

class PredicateTests(BaseGludTest):

    def test_find_classes(self):
        s = '''
        class Foo;
        class Foo {};
        '''
        root = self.parse(s)
        it = glud.walk(is_class, root)
        self.assertEquals(2, count(it))

    def test_can_ignore_forward_declaration(self):
        s = '''
        class Foo;
        class Foo {};
        '''
        root = self.parse(s)
        classes = glud.walk(is_class_definition, root)
        self.assertEquals(1, count(classes))

    def test_template_class(self):
        s = '''
        template<class T> class Foo {};
        '''
        root = self.parse(s)
        classes = glud.walk(is_class, root)
        self.assertEquals(0, count(classes))

    def test_find_nested_classes(self):
        s = '''
        class Foo {
            class Bar {};
        };
        '''
        root = self.parse(s)
        classes = glud.walk(is_class_definition, root)
        classes = list(classes)
        self.assertEquals(2, count(classes))

    def test_find_class_with_named_method(self):
        s = '''
        class Foo {
        public:
            void f();
            void f(int);
        };

        class Bar {
        public:
            void f();
        };

        class Baz {
        public:
            void g();
        };
        '''
        root = self.parse(s)
        f = all_fn([
            is_class_definition,
            any_child(all_fn([
                is_public,
                is_method,
                name_match('f')
            ]))
        ])
        classes = glud.walk(f, root)
        self.assertEquals(2, count(classes))

    def test_enums_types(self):
        s = '''
        enum EmptyEnum {
        };

        enum Bar {
            XXX,
            YYY
        };

        namespace ns {
            enum Baz {
                AAA,
                BBB
            };
        }
        '''
        root = self.parse(s)
        enums = glud.walk(is_enum, root)
        es  = list(enums)
        self.assertEquals('EmptyEnum', es[0].type.spelling)
        self.assertEquals('Bar', es[1].type.spelling)
        self.assertEquals('ns::Baz', es[2].type.spelling)

    def test_methods(self):
        s = '''
        class Foo
        {
        public:
            void f();
        };
        '''
        root = self.parse(s)

        f = all_fn([
            is_in_file(set(['tmp.cpp'])),
            is_method,
            name_match('f'),
        ])
        ms = list(glud.walk(f, root))
        self.assert_(is_primitive(ms[0].result_type))

    def test_access_specifiers(self):
        s = '''
        class foo {
        public:
            void f1();
        protected:
            void g1();
            void g2();
        private: 
            void h1();
            void h2();
            void h3();
        };
        '''
        root = self.parse(s)
        def cnt_match(f, root):
            return count(glud.walk(all_fn([is_method, f]), root))
        self.assertEquals(1, cnt_match(is_public, root))
        self.assertEquals(2, cnt_match(is_protected, root))
        self.assertEquals(3, cnt_match(is_private, root))

    def test_haslocation(self):
        s = 'void f();'
        root = self.parse(s, options=TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD)
        ms = glud.walk(has_location, root)
        list(ms)

    def test_function(self):
        s = '''
        void f();
        '''
        root = self.parse(s)
        fs = glud.walk(is_func, root)
        self.assertEquals(1, count(fs))

    def test_typename_match(self):
        s = '''
        class foo;
        namespace bar {
            class foo;
        }
        '''
        root = self.parse(s)
        fs = glud.walk(typename_match('bar::foo'), root)
        self.assertEquals(1, count(fs))

    def test_any_predecessor(self):
        s = '''
        namespace foo {
            namespace bar {
                class baz {} ;
            }
            class biz {} ;
        }
        '''
        root = self.parse(s)
        f = any_predecessor(lambda c : c.semantic_parent, name_match('bar'))
        classes = glud.walk(all_fn([is_class, f]), root)
        self.assertEquals(1, count(classes))

    def test_all_children(self):
        s = '''
        class foo {
        public:
            int x;
            int y;
        };
        class bar {
        public: 
            int x;
            int y;
        private: 
            int z;
        };
        '''
        root = self.parse(s)
        f = all_fn([
            is_class,
            all_children(is_public)
        ])
        classes = glud.walk(f, root)
        self.assertEquals(1, count(classes))

    def test_any_fn(self):
        s = '''
        class biz {
            void f();
            int g;
            enum baz {};
            class moo {};
        };
        '''
        root = self.parse(s)
        it = glud.walk(any_fn([is_method, is_enum]), root)
        self.assertEquals(2, count(it))


    def test_all_pred(self):
        s = '''
        namespace foo {
            namespace bar {
                class fizz;
            }
            class buzz;
            class mazz;
        }
        '''
        f = all_predecessors(
            lambda s:s.semantic_parent,
            any_fn([
                is_translation_unit,
                all_fn([
                    is_namespace,
                    name_match('foo')
                ])
            ])
        )
        root = self.parse(s)
        it = glud.walk(f, root)
        self.assertEquals(2, count(it))


