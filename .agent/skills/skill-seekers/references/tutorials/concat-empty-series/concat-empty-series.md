# How To: Concat Empty Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat empty series

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series([1, 2, 3], name='x')
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series(name='y', dtype='float64')
```

### Step 3: Assign res = concat(...)

```python
res = concat([s1, s2], axis=1)
```

### Step 4: Assign exp = DataFrame(...)

```python
exp = DataFrame({'x': [1, 2, 3], 'y': [np.nan, np.nan, np.nan]}, index=RangeIndex(3))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```

### Step 6: Assign s1 = Series(...)

```python
s1 = Series([1, 2, 3], name='x')
```

### Step 7: Assign s2 = Series(...)

```python
s2 = Series(name='y', dtype='float64')
```

### Step 8: Assign msg = 'The behavior of array concatenation with empty entries is deprecated'

```python
msg = 'The behavior of array concatenation with empty entries is deprecated'
```

### Step 9: Assign exp = Series(...)

```python
exp = Series([1, 2, 3])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 11: Assign s1 = Series(...)

```python
s1 = Series([1, 2, 3], name='x')
```

### Step 12: Assign s2 = Series(...)

```python
s2 = Series(name=None, dtype='float64')
```

### Step 13: Assign res = concat(...)

```python
res = concat([s1, s2], axis=1)
```

### Step 14: Assign exp = DataFrame(...)

```python
exp = DataFrame({'x': [1, 2, 3], 0: [np.nan, np.nan, np.nan]}, columns=['x', 0], index=RangeIndex(3))
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```

### Step 16: Assign res = concat(...)

```python
res = concat([s1, s2], axis=0)
```


## Complete Example

```python
# Workflow
s1 = Series([1, 2, 3], name='x')
s2 = Series(name='y', dtype='float64')
res = concat([s1, s2], axis=1)
exp = DataFrame({'x': [1, 2, 3], 'y': [np.nan, np.nan, np.nan]}, index=RangeIndex(3))
tm.assert_frame_equal(res, exp)
s1 = Series([1, 2, 3], name='x')
s2 = Series(name='y', dtype='float64')
msg = 'The behavior of array concatenation with empty entries is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = concat([s1, s2], axis=0)
exp = Series([1, 2, 3])
tm.assert_series_equal(res, exp)
s1 = Series([1, 2, 3], name='x')
s2 = Series(name=None, dtype='float64')
res = concat([s1, s2], axis=1)
exp = DataFrame({'x': [1, 2, 3], 0: [np.nan, np.nan, np.nan]}, columns=['x', 0], index=RangeIndex(3))
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_empty.py:54 | Complexity: Advanced | Last updated: 2026-06-02*