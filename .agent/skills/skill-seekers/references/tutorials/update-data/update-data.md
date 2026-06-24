# How To: Update Data

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate dedent_docstring: test update data

## Prerequisites

**Required Modules:**
- `mypy.test.helpers`
- `mypy.test.meta._pytest`


## Step-by-Step Guide

### Step 1: Assign expected = dedent_docstring(...)

```python
expected = dedent_docstring('\n        [case testCorrect]\n        s: str = 42  # E: Incompatible types in assignment (expression has type "int", variable has type "str")\n\n        [case testWrong]\n        s: str = 42  # E: Incompatible types in assignment (expression has type "int", variable has type "str")\n\n        [case testXfail-xfail]\n        s: str = 42  # E: wrong error\n\n        [case testWrongMultiline]\n        s: str = 42  # E: Incompatible types in assignment (expression has type "int", variable has type "str")\n\n        [case testMissingMultiline]\n        s: str = 42;  i: int = \'foo\'  # E: Incompatible types in assignment (expression has type "int", variable has type "str") \\\n                                      # E: Incompatible types in assignment (expression has type "str", variable has type "int")\n\n        [case testExtraneous]\n        s: str = \'foo\'\n\n        [case testExtraneousMultiline]\n        s: str = \'foo\'\n\n        [case testExtraneousMultilineNonError]\n        s: str = \'foo\'\n\n        [case testOutCorrect]\n        s: str = 42\n        [out]\n        main:1: error: Incompatible types in assignment (expression has type "int", variable has type "str")\n\n        [case testOutWrong]\n        s: str = 42\n        [out]\n        main:1: error: Incompatible types in assignment (expression has type "int", variable has type "str")\n\n        [case testOutWrongIncremental]\n        s: str = 42\n        [out]\n        main:1: error: Incompatible types in assignment (expression has type "int", variable has type "str")\n        [out2]\n        main:1: error: Incompatible types in assignment (expression has type "int", variable has type "str")\n\n        [case testWrongMultipleFiles]\n        import a, b\n        s: str = 42  # E: Incompatible types in assignment (expression has type "int", variable has type "str")\n        [file a.py]\n        s1: str = 42  # E: Incompatible types in assignment (expression has type "int", variable has type "str")\n        [file b.py]\n        s2: str = 43  # E: Incompatible types in assignment (expression has type "int", variable has type "str")\n        [builtins fixtures/list.pyi]\n        ')
```


## Complete Example

```python
# Workflow
expected = dedent_docstring('\n        [case testCorrect]\n        s: str = 42  # E: Incompatible types in assignment (expression has type "int", variable has type "str")\n\n        [case testWrong]\n        s: str = 42  # E: Incompatible types in assignment (expression has type "int", variable has type "str")\n\n        [case testXfail-xfail]\n        s: str = 42  # E: wrong error\n\n        [case testWrongMultiline]\n        s: str = 42  # E: Incompatible types in assignment (expression has type "int", variable has type "str")\n\n        [case testMissingMultiline]\n        s: str = 42;  i: int = \'foo\'  # E: Incompatible types in assignment (expression has type "int", variable has type "str") \\\n                                      # E: Incompatible types in assignment (expression has type "str", variable has type "int")\n\n        [case testExtraneous]\n        s: str = \'foo\'\n\n        [case testExtraneousMultiline]\n        s: str = \'foo\'\n\n        [case testExtraneousMultilineNonError]\n        s: str = \'foo\'\n\n        [case testOutCorrect]\n        s: str = 42\n        [out]\n        main:1: error: Incompatible types in assignment (expression has type "int", variable has type "str")\n\n        [case testOutWrong]\n        s: str = 42\n        [out]\n        main:1: error: Incompatible types in assignment (expression has type "int", variable has type "str")\n\n        [case testOutWrongIncremental]\n        s: str = 42\n        [out]\n        main:1: error: Incompatible types in assignment (expression has type "int", variable has type "str")\n        [out2]\n        main:1: error: Incompatible types in assignment (expression has type "int", variable has type "str")\n\n        [case testWrongMultipleFiles]\n        import a, b\n        s: str = 42  # E: Incompatible types in assignment (expression has type "int", variable has type "str")\n        [file a.py]\n        s1: str = 42  # E: Incompatible types in assignment (expression has type "int", variable has type "str")\n        [file b.py]\n        s2: str = 43  # E: Incompatible types in assignment (expression has type "int", variable has type "str")\n        [builtins fixtures/list.pyi]\n        ')
```

## Next Steps


---

*Source: test_update_data.py:81 | Complexity: Beginner | Last updated: 2026-06-02*