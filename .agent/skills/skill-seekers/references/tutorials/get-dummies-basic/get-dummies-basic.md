# How To: Get Dummies Basic

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get dummies basic

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `unicodedata`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`
- `pyarrow`

**Setup Required:**
```python
# Fixtures: sparse, dtype
```

## Step-by-Step Guide

### Step 1: Assign s_list = list(...)

```python
s_list = list('abc')
```

### Step 2: Assign s_series = Series(...)

```python
s_series = Series(s_list)
```

### Step 3: Assign s_series_index = Series(...)

```python
s_series_index = Series(s_list, list('ABC'))
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 0, 0], 'b': [0, 1, 0], 'c': [0, 0, 1]}, dtype=self.effective_dtype(dtype))
```

### Step 5: Assign result = get_dummies(...)

```python
result = get_dummies(s_list, sparse=sparse, dtype=dtype)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = get_dummies(...)

```python
result = get_dummies(s_series, sparse=sparse, dtype=dtype)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign expected.index = list(...)

```python
expected.index = list('ABC')
```

### Step 10: Assign result = get_dummies(...)

```python
result = get_dummies(s_series_index, sparse=sparse, dtype=dtype)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 12: Assign expected = expected.apply(...)

```python
expected = expected.apply(SparseArray, fill_value=False)
```

### Step 13: Assign expected = expected.apply(...)

```python
expected = expected.apply(SparseArray, fill_value=0.0)
```


## Complete Example

```python
# Setup
# Fixtures: sparse, dtype

# Workflow
s_list = list('abc')
s_series = Series(s_list)
s_series_index = Series(s_list, list('ABC'))
expected = DataFrame({'a': [1, 0, 0], 'b': [0, 1, 0], 'c': [0, 0, 1]}, dtype=self.effective_dtype(dtype))
if sparse:
    if dtype.kind == 'b':
        expected = expected.apply(SparseArray, fill_value=False)
    else:
        expected = expected.apply(SparseArray, fill_value=0.0)
result = get_dummies(s_list, sparse=sparse, dtype=dtype)
tm.assert_frame_equal(result, expected)
result = get_dummies(s_series, sparse=sparse, dtype=dtype)
tm.assert_frame_equal(result, expected)
expected.index = list('ABC')
result = get_dummies(s_series_index, sparse=sparse, dtype=dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_get_dummies.py:58 | Complexity: Advanced | Last updated: 2026-06-02*