.. :changelog:

Release History
---------------

0.4.0 (2016-07-23)
++++++++++++++++++

**New Features**

- Added new matchers - parameterCountIs, isExpansionInFileMatching, varDecl,
  hasParent, hasParameter, hasCanonicalType, pointee and pointerType

**Improvements**

- Improved behavior on older versions of libclang
- Moved existing code from the internal API into the stable interface
  (isPublic, isProtected, isPrivate) 

**Bug Fixes**

- Corrected the behavior of recordDecl and cxxRecordDecl to more closely map to
  the libclangastmatchers vision of those matchers
- Corrected the name of anyArgument to hasAnyParameter
