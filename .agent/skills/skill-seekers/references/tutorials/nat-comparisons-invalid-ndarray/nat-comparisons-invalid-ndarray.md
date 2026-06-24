# How To: Nat Comparisons Invalid Ndarray

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nat comparisons invalid ndarray

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: other
```

## Step-by-Step Guide

### Step 1: Assign expected = np.array(...)

```python
expected = np.array([False, False])
```

### Step 2: Assign result = value

```python
result = NaT == other
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 4: Assign result = value

```python
result = other == NaT
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([True, True])
```

### Step 7: Assign result = value

```python
result = NaT != other
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 9: Assign result = value

```python
result = other != NaT
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 11: Assign msg = value

```python
msg = f"'{symbol}' not supported between"
```

### Step 12: Call op()

```python
op(NaT, other)
```

### Step 13: Assign msg = None

```python
msg = None
```

### Step 14: Call op()

```python
op(other, NaT)
```


## Complete Example

```python
# Setup
# Fixtures: other

# Workflow
expected = np.array([False, False])
result = NaT == other
tm.assert_numpy_array_equal(result, expected)
result = other == NaT
tm.assert_numpy_array_equal(result, expected)
expected = np.array([True, True])
result = NaT != other
tm.assert_numpy_array_equal(result, expected)
result = other != NaT
tm.assert_numpy_array_equal(result, expected)
for symbol, op in [('<=', operator.le), ('<', operator.lt), ('>=', operator.ge), ('>', operator.gt)]:
    msg = f"'{symbol}' not supported between"
    with pytest.raises(TypeError, match=msg):
        op(NaT, other)
    if other.dtype == np.dtype('object'):
        msg = None
    with pytest.raises(TypeError, match=msg):
        op(other, NaT)
```

## Next Steps


---

*Source: test_nat.py:618 | Complexity: Advanced | Last updated: 2026-06-02*