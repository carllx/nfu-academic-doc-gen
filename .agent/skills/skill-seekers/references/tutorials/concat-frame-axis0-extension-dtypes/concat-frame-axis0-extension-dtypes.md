# How To: Concat Frame Axis0 Extension Dtypes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat frame axis0 extension dtypes

## Prerequisites

**Required Modules:**
- `collections`
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.extension.decimal`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'a': pd.array([1, 2, 3], dtype='Int64')})
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'a': np.array([4, 5, 6])})
```

### Step 3: Assign result = concat(...)

```python
result = concat([df1, df2], ignore_index=True)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2, 3, 4, 5, 6]}, dtype='Int64')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = concat(...)

```python
result = concat([df2, df1], ignore_index=True)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [4, 5, 6, 1, 2, 3]}, dtype='Int64')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'a': pd.array([1, 2, 3], dtype='Int64')})
df2 = DataFrame({'a': np.array([4, 5, 6])})
result = concat([df1, df2], ignore_index=True)
expected = DataFrame({'a': [1, 2, 3, 4, 5, 6]}, dtype='Int64')
tm.assert_frame_equal(result, expected)
result = concat([df2, df1], ignore_index=True)
expected = DataFrame({'a': [4, 5, 6, 1, 2, 3]}, dtype='Int64')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_concat.py:645 | Complexity: Advanced | Last updated: 2026-06-02*