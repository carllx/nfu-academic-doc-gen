# How To: Comp Nat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test comp nat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign left = TimedeltaIndex(...)

```python
left = TimedeltaIndex([Timedelta('1 days'), NaT, Timedelta('3 days')])
```

### Step 2: Assign right = TimedeltaIndex(...)

```python
right = TimedeltaIndex([NaT, NaT, Timedelta('3 days')])
```

### Step 3: Assign unknown = value

```python
lhs, rhs = (left, right)
```

### Step 4: Assign result = value

```python
result = rhs == lhs
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([False, False, True])
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = rhs != lhs
```

### Step 8: Assign expected = np.array(...)

```python
expected = np.array([True, True, False])
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 10: Assign expected = np.array(...)

```python
expected = np.array([False, False, False])
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lhs == NaT, expected)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(NaT == rhs, expected)
```

### Step 13: Assign expected = np.array(...)

```python
expected = np.array([True, True, True])
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lhs != NaT, expected)
```

### Step 15: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(NaT != lhs, expected)
```

### Step 16: Assign expected = np.array(...)

```python
expected = np.array([False, False, False])
```

### Step 17: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lhs < NaT, expected)
```

### Step 18: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(NaT > lhs, expected)
```

### Step 19: Assign unknown = value

```python
lhs, rhs = (left.astype(object), right.astype(object))
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
left = TimedeltaIndex([Timedelta('1 days'), NaT, Timedelta('3 days')])
right = TimedeltaIndex([NaT, NaT, Timedelta('3 days')])
lhs, rhs = (left, right)
if dtype is object:
    lhs, rhs = (left.astype(object), right.astype(object))
result = rhs == lhs
expected = np.array([False, False, True])
tm.assert_numpy_array_equal(result, expected)
result = rhs != lhs
expected = np.array([True, True, False])
tm.assert_numpy_array_equal(result, expected)
expected = np.array([False, False, False])
tm.assert_numpy_array_equal(lhs == NaT, expected)
tm.assert_numpy_array_equal(NaT == rhs, expected)
expected = np.array([True, True, True])
tm.assert_numpy_array_equal(lhs != NaT, expected)
tm.assert_numpy_array_equal(NaT != lhs, expected)
expected = np.array([False, False, False])
tm.assert_numpy_array_equal(lhs < NaT, expected)
tm.assert_numpy_array_equal(NaT > lhs, expected)
```

## Next Steps


---

*Source: test_timedelta64.py:174 | Complexity: Advanced | Last updated: 2026-06-02*