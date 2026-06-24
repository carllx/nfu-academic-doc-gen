# How To: Coerce To Array

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test coerce to array

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `pandas.core.arrays.boolean`


## Step-by-Step Guide

### Step 1: Assign values = np.array(...)

```python
values = np.array([True, False, True, False], dtype='bool')
```

**Verification:**
```python
assert result._data is values
```

### Step 2: Assign mask = np.array(...)

```python
mask = np.array([False, False, False, True], dtype='bool')
```

**Verification:**
```python
assert result._mask is mask
```

### Step 3: Assign result = BooleanArray(...)

```python
result = BooleanArray(*coerce_to_array(values, mask=mask))
```

**Verification:**
```python
assert result._data is not values
```

### Step 4: Assign expected = BooleanArray(...)

```python
expected = BooleanArray(values, mask)
```

**Verification:**
```python
assert result._mask is not mask
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

**Verification:**
```python
assert result._data is values
```

### Step 6: Assign result = BooleanArray(...)

```python
result = BooleanArray(*coerce_to_array(values, mask=mask, copy=True))
```

### Step 7: Assign expected = BooleanArray(...)

```python
expected = BooleanArray(values, mask)
```

### Step 8: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

**Verification:**
```python
assert result._data is not values
```

### Step 9: Assign values = value

```python
values = [True, False, None, False]
```

### Step 10: Assign mask = np.array(...)

```python
mask = np.array([False, False, False, True], dtype='bool')
```

### Step 11: Assign result = BooleanArray(...)

```python
result = BooleanArray(*coerce_to_array(values, mask=mask))
```

### Step 12: Assign expected = BooleanArray(...)

```python
expected = BooleanArray(np.array([True, False, True, True]), np.array([False, False, True, True]))
```

### Step 13: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 14: Assign result = BooleanArray(...)

```python
result = BooleanArray(*coerce_to_array(np.array(values, dtype=object), mask=mask))
```

### Step 15: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 16: Assign result = BooleanArray(...)

```python
result = BooleanArray(*coerce_to_array(values, mask=mask.tolist()))
```

### Step 17: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 18: Assign values = np.array(...)

```python
values = np.array([True, False, True, False], dtype='bool')
```

### Step 19: Assign mask = np.array(...)

```python
mask = np.array([False, False, False, True], dtype='bool')
```

### Step 20: Call coerce_to_array()

```python
coerce_to_array(values.reshape(1, -1))
```

### Step 21: Call coerce_to_array()

```python
coerce_to_array(values.reshape(1, -1), mask=mask)
```

### Step 22: Call coerce_to_array()

```python
coerce_to_array(values, mask=mask.reshape(1, -1))
```


## Complete Example

```python
# Workflow
values = np.array([True, False, True, False], dtype='bool')
mask = np.array([False, False, False, True], dtype='bool')
result = BooleanArray(*coerce_to_array(values, mask=mask))
expected = BooleanArray(values, mask)
tm.assert_extension_array_equal(result, expected)
assert result._data is values
assert result._mask is mask
result = BooleanArray(*coerce_to_array(values, mask=mask, copy=True))
expected = BooleanArray(values, mask)
tm.assert_extension_array_equal(result, expected)
assert result._data is not values
assert result._mask is not mask
values = [True, False, None, False]
mask = np.array([False, False, False, True], dtype='bool')
result = BooleanArray(*coerce_to_array(values, mask=mask))
expected = BooleanArray(np.array([True, False, True, True]), np.array([False, False, True, True]))
tm.assert_extension_array_equal(result, expected)
result = BooleanArray(*coerce_to_array(np.array(values, dtype=object), mask=mask))
tm.assert_extension_array_equal(result, expected)
result = BooleanArray(*coerce_to_array(values, mask=mask.tolist()))
tm.assert_extension_array_equal(result, expected)
values = np.array([True, False, True, False], dtype='bool')
mask = np.array([False, False, False, True], dtype='bool')
coerce_to_array(values.reshape(1, -1))
with pytest.raises(ValueError, match='values.shape and mask.shape must match'):
    coerce_to_array(values.reshape(1, -1), mask=mask)
with pytest.raises(ValueError, match='values.shape and mask.shape must match'):
    coerce_to_array(values, mask=mask.reshape(1, -1))
```

## Next Steps


---

*Source: test_construction.py:154 | Complexity: Advanced | Last updated: 2026-06-02*