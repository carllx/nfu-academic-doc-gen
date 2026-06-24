# How To: Boolean Array Constructor

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test boolean array constructor

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

### Step 2: Assign mask = np.array(...)

```python
mask = np.array([False, False, False, True], dtype='bool')
```

### Step 3: Assign result = BooleanArray(...)

```python
result = BooleanArray(values, mask)
```

### Step 4: Assign expected = pd.array(...)

```python
expected = pd.array([True, False, True, None], dtype='boolean')
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 6: Call BooleanArray()

```python
BooleanArray(values.tolist(), mask)
```

### Step 7: Call BooleanArray()

```python
BooleanArray(values, mask.tolist())
```

### Step 8: Call BooleanArray()

```python
BooleanArray(values.astype(int), mask)
```

### Step 9: Call BooleanArray()

```python
BooleanArray(values, None)
```

### Step 10: Call BooleanArray()

```python
BooleanArray(values.reshape(1, -1), mask)
```

### Step 11: Call BooleanArray()

```python
BooleanArray(values, mask.reshape(1, -1))
```


## Complete Example

```python
# Workflow
values = np.array([True, False, True, False], dtype='bool')
mask = np.array([False, False, False, True], dtype='bool')
result = BooleanArray(values, mask)
expected = pd.array([True, False, True, None], dtype='boolean')
tm.assert_extension_array_equal(result, expected)
with pytest.raises(TypeError, match='values should be boolean numpy array'):
    BooleanArray(values.tolist(), mask)
with pytest.raises(TypeError, match='mask should be boolean numpy array'):
    BooleanArray(values, mask.tolist())
with pytest.raises(TypeError, match='values should be boolean numpy array'):
    BooleanArray(values.astype(int), mask)
with pytest.raises(TypeError, match='mask should be boolean numpy array'):
    BooleanArray(values, None)
with pytest.raises(ValueError, match='values.shape must match mask.shape'):
    BooleanArray(values.reshape(1, -1), mask)
with pytest.raises(ValueError, match='values.shape must match mask.shape'):
    BooleanArray(values, mask.reshape(1, -1))
```

## Next Steps


---

*Source: test_construction.py:10 | Complexity: Advanced | Last updated: 2026-06-02*