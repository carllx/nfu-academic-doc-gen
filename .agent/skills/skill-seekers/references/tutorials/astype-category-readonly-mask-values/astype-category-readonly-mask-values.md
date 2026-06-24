# How To: Astype Category Readonly Mask Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype category readonly mask values

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = array(...)

```python
arr = array([0, 1, 2], dtype='Int64')
```

### Step 2: Assign unknown = False

```python
arr._mask.flags['WRITEABLE'] = False
```

### Step 3: Assign result = arr.astype(...)

```python
result = arr.astype('category')
```

### Step 4: Assign expected = array.astype(...)

```python
expected = array([0, 1, 2], dtype='Int64').astype('category')
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = array([0, 1, 2], dtype='Int64')
arr._mask.flags['WRITEABLE'] = False
result = arr.astype('category')
expected = array([0, 1, 2], dtype='Int64').astype('category')
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_astype.py:149 | Complexity: Intermediate | Last updated: 2026-06-02*