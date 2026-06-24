# How To: Apply Standard Nonunique

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply standard nonunique

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['a', 'a', 'c'])
```

### Step 2: Assign result = df.apply(...)

```python
result = df.apply(lambda s: s[0], axis=1)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([1, 4, 7], ['a', 'a', 'c'])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = df.T.apply(...)

```python
result = df.T.apply(lambda s: s[0], axis=0)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['a', 'a', 'c'])
result = df.apply(lambda s: s[0], axis=1)
expected = Series([1, 4, 7], ['a', 'a', 'c'])
tm.assert_series_equal(result, expected)
result = df.T.apply(lambda s: s[0], axis=0)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_frame_apply.py:199 | Complexity: Intermediate | Last updated: 2026-06-02*