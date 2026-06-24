# How To: Compare Mismatched Resolutions

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare mismatched resolutions

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `zoneinfo`

**Setup Required:**
```python
# Fixtures: comparison_op
```

## Step-by-Step Guide

### Step 1: Assign op = comparison_op

```python
op = comparison_op
```

### Step 2: Assign iinfo = np.iinfo(...)

```python
iinfo = np.iinfo(np.int64)
```

### Step 3: Assign vals = np.array(...)

```python
vals = np.array([iinfo.min, iinfo.min + 1, iinfo.max], dtype=np.int64)
```

### Step 4: Assign arr = np.array.view(...)

```python
arr = np.array(vals).view('M8[ns]')
```

### Step 5: Assign arr2 = arr.view(...)

```python
arr2 = arr.view('M8[s]')
```

### Step 6: Assign left = DatetimeArray._simple_new(...)

```python
left = DatetimeArray._simple_new(arr, dtype=arr.dtype)
```

### Step 7: Assign right = DatetimeArray._simple_new(...)

```python
right = DatetimeArray._simple_new(arr2, dtype=arr2.dtype)
```

### Step 8: Assign result = op(...)

```python
result = op(left, right)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 10: Assign result = op(...)

```python
result = op(left[1], right)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 12: Assign expected = np.array(...)

```python
expected = np.array([False, False, False])
```

### Step 13: Assign np_res = op(...)

```python
np_res = op(left._ndarray, right._ndarray)
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np_res[1:], ~expected[1:])
```

### Step 15: Assign expected = np.array(...)

```python
expected = np.array([True, True, True])
```

### Step 16: Assign expected = np.array(...)

```python
expected = np.array([False, False, True])
```

### Step 17: Assign expected = np.array(...)

```python
expected = np.array([False, True, False])
```


## Complete Example

```python
# Setup
# Fixtures: comparison_op

# Workflow
op = comparison_op
iinfo = np.iinfo(np.int64)
vals = np.array([iinfo.min, iinfo.min + 1, iinfo.max], dtype=np.int64)
arr = np.array(vals).view('M8[ns]')
arr2 = arr.view('M8[s]')
left = DatetimeArray._simple_new(arr, dtype=arr.dtype)
right = DatetimeArray._simple_new(arr2, dtype=arr2.dtype)
if comparison_op is operator.eq:
    expected = np.array([False, False, False])
elif comparison_op is operator.ne:
    expected = np.array([True, True, True])
elif comparison_op in [operator.lt, operator.le]:
    expected = np.array([False, False, True])
else:
    expected = np.array([False, True, False])
result = op(left, right)
tm.assert_numpy_array_equal(result, expected)
result = op(left[1], right)
tm.assert_numpy_array_equal(result, expected)
if op not in [operator.eq, operator.ne]:
    np_res = op(left._ndarray, right._ndarray)
    tm.assert_numpy_array_equal(np_res[1:], ~expected[1:])
```

## Next Steps


---

*Source: test_datetimes.py:174 | Complexity: Advanced | Last updated: 2026-06-02*