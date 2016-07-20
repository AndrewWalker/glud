.. :changelog:

Release History
---------------

0.4.0 (2016-07-17)
++++++++++++++++++

**New Features**

- Added new matchers - parameterCountIs, isExpansionInFileMatching, varDecl and
  hasParent, hasCanonicalType

**Improvements**

- Improved behavior on older versions of libclang
- Moved existing predicates (isPublic, isProtected, isPrivate) into the matchers
