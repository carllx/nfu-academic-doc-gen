# How To: Astype To Floating Array

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype to floating array

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = pd.array(...)

```python
arr = pd.array([0.0, 1.0, None], dtype='Float64')
```

### Step 2: Assign result = arr.astype(...)

```python
result = arr.astype('Float64')
```

### Step 3: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, arr)
```

### Step 4: Assign result = arr.astype(...)

```python
result = arr.astype(pd.Float64Dtype())
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, arr)
```

### Step 6: Assign result = arr.astype(...)

```python
result = arr.astype('Float32')
```

### Step 7: Assign expected = pd.array(...)

```python
expected = pd.array([0.0, 1.0, None], dtype='Float32')
```

### Step 8: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = pd.array([0.0, 1.0, None], dtype='Float64')
result = arr.astype('Float64')
tm.assert_extension_array_equal(result, arr)
result = arr.astype(pd.Float64Dtype())
tm.assert_extension_array_equal(result, arr)
result = arr.astype('Float32')
expected = pd.array([0.0, 1.0, None], dtype='Float32')
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_astype.py:33 | Complexity: Advanced | Last updated: 2026-06-02*