# How To: Comparison Dt64 Ndarray Tzaware

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test comparison dt64 ndarray tzaware

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: reverse, comparison_op
```

## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('2021-01-01 00:00:00.00000', tz='UTC')
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array([ts.asm8, ts.asm8], dtype='M8[ns]')
```

### Step 3: Assign unknown = value

```python
left, right = (ts, arr)
```

### Step 4: Assign unknown = value

```python
left, right = (arr, ts)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([False, False], dtype=bool)
```

### Step 6: Assign result = comparison_op(...)

```python
result = comparison_op(left, right)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 8: Assign expected = np.array(...)

```python
expected = np.array([True, True], dtype=bool)
```

### Step 9: Assign result = comparison_op(...)

```python
result = comparison_op(left, right)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 11: Assign msg = 'Cannot compare tz-naive and tz-aware timestamps'

```python
msg = 'Cannot compare tz-naive and tz-aware timestamps'
```

### Step 12: Call comparison_op()

```python
comparison_op(left, right)
```


## Complete Example

```python
# Setup
# Fixtures: reverse, comparison_op

# Workflow
ts = Timestamp('2021-01-01 00:00:00.00000', tz='UTC')
arr = np.array([ts.asm8, ts.asm8], dtype='M8[ns]')
left, right = (ts, arr)
if reverse:
    left, right = (arr, ts)
if comparison_op is operator.eq:
    expected = np.array([False, False], dtype=bool)
    result = comparison_op(left, right)
    tm.assert_numpy_array_equal(result, expected)
elif comparison_op is operator.ne:
    expected = np.array([True, True], dtype=bool)
    result = comparison_op(left, right)
    tm.assert_numpy_array_equal(result, expected)
else:
    msg = 'Cannot compare tz-naive and tz-aware timestamps'
    with pytest.raises(TypeError, match=msg):
        comparison_op(left, right)
```

## Next Steps


---

*Source: test_comparisons.py:59 | Complexity: Advanced | Last updated: 2026-06-02*