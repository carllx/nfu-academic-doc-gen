# How To: Comparisons Nat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test comparisons nat

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
# Fixtures: idx2
```

## Step-by-Step Guide

### Step 1: Assign idx1 = TimedeltaIndex(...)

```python
idx1 = TimedeltaIndex(['1 day', NaT, '1 day 00:00:01', NaT, '1 day 00:00:01', '5 day 00:00:03'])
```

### Step 2: Assign result = value

```python
result = idx1 < idx2
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([True, False, False, False, True, False])
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = idx2 > idx1
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([True, False, False, False, True, False])
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = idx1 <= idx2
```

### Step 9: Assign expected = np.array(...)

```python
expected = np.array([True, False, False, False, True, True])
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 11: Assign result = value

```python
result = idx2 >= idx1
```

### Step 12: Assign expected = np.array(...)

```python
expected = np.array([True, False, False, False, True, True])
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 14: Assign result = value

```python
result = idx1 == idx2
```

### Step 15: Assign expected = np.array(...)

```python
expected = np.array([False, False, False, False, False, True])
```

### Step 16: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 17: Assign result = value

```python
result = idx1 != idx2
```

### Step 18: Assign expected = np.array(...)

```python
expected = np.array([True, True, True, True, True, False])
```

### Step 19: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: idx2

# Workflow
idx1 = TimedeltaIndex(['1 day', NaT, '1 day 00:00:01', NaT, '1 day 00:00:01', '5 day 00:00:03'])
result = idx1 < idx2
expected = np.array([True, False, False, False, True, False])
tm.assert_numpy_array_equal(result, expected)
result = idx2 > idx1
expected = np.array([True, False, False, False, True, False])
tm.assert_numpy_array_equal(result, expected)
result = idx1 <= idx2
expected = np.array([True, False, False, False, True, True])
tm.assert_numpy_array_equal(result, expected)
result = idx2 >= idx1
expected = np.array([True, False, False, False, True, True])
tm.assert_numpy_array_equal(result, expected)
result = idx1 == idx2
expected = np.array([False, False, False, False, False, True])
tm.assert_numpy_array_equal(result, expected)
result = idx1 != idx2
expected = np.array([True, True, True, True, True, False])
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_timedelta64.py:220 | Complexity: Advanced | Last updated: 2026-06-02*