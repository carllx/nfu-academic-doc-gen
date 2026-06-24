# How To: Apply Bug

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply bug

## Prerequisites

**Required Modules:**
- `datetime`
- `warnings`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.frame.common`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign positions = DataFrame(...)

```python
positions = DataFrame([[1, 'ABC0', 50], [1, 'YUM0', 20], [1, 'DEF0', 20], [2, 'ABC1', 50], [2, 'YUM1', 20], [2, 'DEF1', 20]], columns=['a', 'market', 'position'])
```

### Step 2: Assign expected = positions.apply(...)

```python
expected = positions.apply(f, axis=1)
```

### Step 3: Assign positions = DataFrame(...)

```python
positions = DataFrame([[datetime(2013, 1, 1), 'ABC0', 50], [datetime(2013, 1, 2), 'YUM0', 20], [datetime(2013, 1, 3), 'DEF0', 20], [datetime(2013, 1, 4), 'ABC1', 50], [datetime(2013, 1, 5), 'YUM1', 20], [datetime(2013, 1, 6), 'DEF1', 20]], columns=['a', 'market', 'position'])
```

### Step 4: Assign result = positions.apply(...)

```python
result = positions.apply(f, axis=1)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
positions = DataFrame([[1, 'ABC0', 50], [1, 'YUM0', 20], [1, 'DEF0', 20], [2, 'ABC1', 50], [2, 'YUM1', 20], [2, 'DEF1', 20]], columns=['a', 'market', 'position'])

def f(r):
    return r['market']
expected = positions.apply(f, axis=1)
positions = DataFrame([[datetime(2013, 1, 1), 'ABC0', 50], [datetime(2013, 1, 2), 'YUM0', 20], [datetime(2013, 1, 3), 'DEF0', 20], [datetime(2013, 1, 4), 'ABC1', 50], [datetime(2013, 1, 5), 'YUM1', 20], [datetime(2013, 1, 6), 'DEF1', 20]], columns=['a', 'market', 'position'])
result = positions.apply(f, axis=1)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_frame_apply.py:441 | Complexity: Intermediate | Last updated: 2026-06-02*