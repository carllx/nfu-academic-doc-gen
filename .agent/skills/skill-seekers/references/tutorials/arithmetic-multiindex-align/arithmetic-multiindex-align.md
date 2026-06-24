# How To: Arithmetic Multiindex Align

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Regression test for: https://github.com/pandas-dev/pandas/issues/33765

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `enum`
- `functools`
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.computation`
- `pandas.tests.frame.common`


## Step-by-Step Guide

### Step 1: '\n    Regression test for: https://github.com/pandas-dev/pandas/issues/33765\n    '

```python
'\n    Regression test for: https://github.com/pandas-dev/pandas/issues/33765\n    '
```

### Step 2: Assign df1 = DataFrame(...)

```python
df1 = DataFrame([[1]], index=['a'], columns=MultiIndex.from_product([[0], [1]], names=['a', 'b']))
```

### Step 3: Assign df2 = DataFrame(...)

```python
df2 = DataFrame([[1]], index=['a'], columns=Index([0], name='a'))
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[0]], index=['a'], columns=MultiIndex.from_product([[0], [1]], names=['a', 'b']))
```

### Step 5: Assign result = value

```python
result = df1 - df2
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
'\n    Regression test for: https://github.com/pandas-dev/pandas/issues/33765\n    '
df1 = DataFrame([[1]], index=['a'], columns=MultiIndex.from_product([[0], [1]], names=['a', 'b']))
df2 = DataFrame([[1]], index=['a'], columns=Index([0], name='a'))
expected = DataFrame([[0]], index=['a'], columns=MultiIndex.from_product([[0], [1]], names=['a', 'b']))
result = df1 - df2
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:2043 | Complexity: Intermediate | Last updated: 2026-06-02*