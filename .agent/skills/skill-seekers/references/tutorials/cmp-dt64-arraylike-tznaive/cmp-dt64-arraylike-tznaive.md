# How To: Cmp Dt64 Arraylike Tznaive

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cmp dt64 arraylike tznaive

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

**Verification:**
```python
assert arr.freq == dti.freq
```

### Step 2: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('2016-01-1', freq='MS', periods=9, tz=None)
```

**Verification:**
```python
assert arr.tz == dti.tz
```

### Step 3: Assign arr = value

```python
arr = dti._data
```

**Verification:**
```python
assert arr.freq == dti.freq
```

### Step 4: Assign right = dti

```python
right = dti
```

### Step 5: Assign expected = np.ones(...)

```python
expected = np.ones(len(arr), dtype=bool)
```

### Step 6: Assign result = op(...)

```python
result = op(arr, arr)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 8: Assign expected = value

```python
expected = ~expected
```

### Step 9: Assign result = op(...)

```python
result = op(arr, other)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 11: Assign result = op(...)

```python
result = op(other, arr)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: comparison_op

# Workflow
op = comparison_op
dti = pd.date_range('2016-01-1', freq='MS', periods=9, tz=None)
arr = dti._data
assert arr.freq == dti.freq
assert arr.tz == dti.tz
right = dti
expected = np.ones(len(arr), dtype=bool)
if comparison_op.__name__ in ['ne', 'gt', 'lt']:
    expected = ~expected
result = op(arr, arr)
tm.assert_numpy_array_equal(result, expected)
for other in [right, np.array(right), list(right), tuple(right), right.astype(object)]:
    result = op(arr, other)
    tm.assert_numpy_array_equal(result, expected)
    result = op(other, arr)
    tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimes.py:279 | Complexity: Advanced | Last updated: 2026-06-02*