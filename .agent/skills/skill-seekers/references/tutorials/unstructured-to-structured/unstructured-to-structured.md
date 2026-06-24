# How To: Unstructured To Structured

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unstructured to structured

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.ma`
- `numpy.lib.recfunctions`
- `numpy.ma.mrecords`
- `numpy.ma.testutils`
- `numpy.testing`
- `datetime`


## Step-by-Step Guide

### Step 1: Assign a = np.zeros(...)

```python
a = np.zeros((20, 2))
```

**Verification:**
```python
assert_equal(field1, field2)
```

### Step 2: Assign test_dtype_args = value

```python
test_dtype_args = [('x', float), ('y', float)]
```

### Step 3: Assign test_dtype = np.dtype(...)

```python
test_dtype = np.dtype(test_dtype_args)
```

### Step 4: Assign field1 = unstructured_to_structured(...)

```python
field1 = unstructured_to_structured(a, dtype=test_dtype_args)
```

### Step 5: Assign field2 = unstructured_to_structured(...)

```python
field2 = unstructured_to_structured(a, dtype=test_dtype)
```

### Step 6: Call assert_equal()

```python
assert_equal(field1, field2)
```


## Complete Example

```python
# Workflow
a = np.zeros((20, 2))
test_dtype_args = [('x', float), ('y', float)]
test_dtype = np.dtype(test_dtype_args)
field1 = unstructured_to_structured(a, dtype=test_dtype_args)
field2 = unstructured_to_structured(a, dtype=test_dtype)
assert_equal(field1, field2)
```

## Next Steps


---

*Source: test_recfunctions.py:385 | Complexity: Intermediate | Last updated: 2026-06-02*