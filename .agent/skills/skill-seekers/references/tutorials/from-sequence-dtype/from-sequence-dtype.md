# How To: From Sequence Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from sequence dtype

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([1, 2, 3], dtype='int64')
```

### Step 2: Assign result = NumpyExtensionArray._from_sequence(...)

```python
result = NumpyExtensionArray._from_sequence(arr, dtype='uint64')
```

### Step 3: Assign expected = NumpyExtensionArray(...)

```python
expected = NumpyExtensionArray(np.array([1, 2, 3], dtype='uint64'))
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = np.array([1, 2, 3], dtype='int64')
result = NumpyExtensionArray._from_sequence(arr, dtype='uint64')
expected = NumpyExtensionArray(np.array([1, 2, 3], dtype='uint64'))
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_numpy.py:120 | Complexity: Intermediate | Last updated: 2026-06-02*