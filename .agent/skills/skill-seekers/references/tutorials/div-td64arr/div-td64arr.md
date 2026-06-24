# How To: Div Td64Arr

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test div td64arr

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `collections`
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: left, box_cls
```

## Step-by-Step Guide

### Step 1: Assign right = np.array(...)

```python
right = np.array([10, 40, 90], dtype='m8[s]')
```

**Verification:**
```python
assert expected.dtype == right.dtype
```

### Step 2: Assign right = box_cls(...)

```python
right = box_cls(right)
```

### Step 3: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex(['1s', '2s', '3s'], dtype=right.dtype)
```

**Verification:**
```python
assert expected.dtype == right.dtype
```

### Step 4: Assign result = value

```python
result = right / left
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = right // left
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 8: Assign msg = "ufunc '(true_)?divide' cannot use operands with types"

```python
msg = "ufunc '(true_)?divide' cannot use operands with types"
```

### Step 9: Assign msg = "ufunc 'floor_divide' cannot use operands with types"

```python
msg = "ufunc 'floor_divide' cannot use operands with types"
```

### Step 10: Assign expected = Series(...)

```python
expected = Series(expected)
```

### Step 11: left / right

```python
left / right
```

### Step 12: left // right

```python
left // right
```


## Complete Example

```python
# Setup
# Fixtures: left, box_cls

# Workflow
right = np.array([10, 40, 90], dtype='m8[s]')
right = box_cls(right)
expected = TimedeltaIndex(['1s', '2s', '3s'], dtype=right.dtype)
if isinstance(left, Series) or box_cls is Series:
    expected = Series(expected)
assert expected.dtype == right.dtype
result = right / left
tm.assert_equal(result, expected)
result = right // left
tm.assert_equal(result, expected)
msg = "ufunc '(true_)?divide' cannot use operands with types"
with pytest.raises(TypeError, match=msg):
    left / right
msg = "ufunc 'floor_divide' cannot use operands with types"
with pytest.raises(TypeError, match=msg):
    left // right
```

## Next Steps


---

*Source: test_numeric.py:198 | Complexity: Advanced | Last updated: 2026-06-02*