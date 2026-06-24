# How To: Logical Operators Int Dtype With Int Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test logical operators int dtype with int dtype

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign s_0123 = Series(...)

```python
s_0123 = Series(range(4), dtype='int64')
```

### Step 2: Assign s_3333 = Series(...)

```python
s_3333 = Series([3] * 4)
```

### Step 3: Assign s_4444 = Series(...)

```python
s_4444 = Series([4] * 4)
```

### Step 4: Assign res = value

```python
res = s_0123 & s_3333
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(range(4), dtype='int64')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 7: Assign res = value

```python
res = s_0123 | s_4444
```

### Step 8: Assign expected = Series(...)

```python
expected = Series(range(4, 8), dtype='int64')
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 10: Assign s_1111 = Series(...)

```python
s_1111 = Series([1] * 4, dtype='int8')
```

### Step 11: Assign res = value

```python
res = s_0123 & s_1111
```

### Step 12: Assign expected = Series(...)

```python
expected = Series([0, 1, 0, 1], dtype='int64')
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 14: Assign res = value

```python
res = s_0123.astype(np.int16) | s_1111.astype(np.int32)
```

### Step 15: Assign expected = Series(...)

```python
expected = Series([1, 1, 3, 3], dtype='int32')
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```


## Complete Example

```python
# Workflow
s_0123 = Series(range(4), dtype='int64')
s_3333 = Series([3] * 4)
s_4444 = Series([4] * 4)
res = s_0123 & s_3333
expected = Series(range(4), dtype='int64')
tm.assert_series_equal(res, expected)
res = s_0123 | s_4444
expected = Series(range(4, 8), dtype='int64')
tm.assert_series_equal(res, expected)
s_1111 = Series([1] * 4, dtype='int8')
res = s_0123 & s_1111
expected = Series([0, 1, 0, 1], dtype='int64')
tm.assert_series_equal(res, expected)
res = s_0123.astype(np.int16) | s_1111.astype(np.int32)
expected = Series([1, 1, 3, 3], dtype='int32')
tm.assert_series_equal(res, expected)
```

## Next Steps


---

*Source: test_logical_ops.py:54 | Complexity: Advanced | Last updated: 2026-06-02*