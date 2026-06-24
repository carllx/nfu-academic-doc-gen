# How To: Apply With Reduce Empty

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply with reduce empty

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

### Step 1: Assign empty_frame = DataFrame(...)

```python
empty_frame = DataFrame()
```

**Verification:**
```python
assert x == []
```

### Step 2: Assign x = value

```python
x = []
```

### Step 3: Assign result = empty_frame.apply(...)

```python
result = empty_frame.apply(x.append, axis=1, result_type='expand')
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, empty_frame)
```

### Step 5: Assign result = empty_frame.apply(...)

```python
result = empty_frame.apply(x.append, axis=1, result_type='reduce')
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([], dtype=np.float64)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign empty_with_cols = DataFrame(...)

```python
empty_with_cols = DataFrame(columns=['a', 'b', 'c'])
```

### Step 9: Assign result = empty_with_cols.apply(...)

```python
result = empty_with_cols.apply(x.append, axis=1, result_type='expand')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, empty_with_cols)
```

### Step 11: Assign result = empty_with_cols.apply(...)

```python
result = empty_with_cols.apply(x.append, axis=1, result_type='reduce')
```

### Step 12: Assign expected = Series(...)

```python
expected = Series([], dtype=np.float64)
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

**Verification:**
```python
assert x == []
```


## Complete Example

```python
# Workflow
empty_frame = DataFrame()
x = []
result = empty_frame.apply(x.append, axis=1, result_type='expand')
tm.assert_frame_equal(result, empty_frame)
result = empty_frame.apply(x.append, axis=1, result_type='reduce')
expected = Series([], dtype=np.float64)
tm.assert_series_equal(result, expected)
empty_with_cols = DataFrame(columns=['a', 'b', 'c'])
result = empty_with_cols.apply(x.append, axis=1, result_type='expand')
tm.assert_frame_equal(result, empty_with_cols)
result = empty_with_cols.apply(x.append, axis=1, result_type='reduce')
expected = Series([], dtype=np.float64)
tm.assert_series_equal(result, expected)
assert x == []
```

## Next Steps


---

*Source: test_frame_apply.py:152 | Complexity: Advanced | Last updated: 2026-06-02*