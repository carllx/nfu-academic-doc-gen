# How To: Gh 26542 Index Overlap

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test gh 26542 index overlap

## Prerequisites

**Required Modules:**
- `functools`
- `inspect`
- `operator`
- `sys`
- `warnings`
- `itertools`
- `pytest`
- `numpy`
- `numpy._core._multiarray_tests`
- `numpy.exceptions`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.arange(...)

```python
arr = np.arange(100)
```

**Verification:**
```python
assert_equal(actual_vals, expected_vals)
```

### Step 2: Assign expected_vals = np.copy(...)

```python
expected_vals = np.copy(arr[:-10])
```

### Step 3: Assign unknown = value

```python
arr[10:] = arr[:-10]
```

### Step 4: Assign actual_vals = value

```python
actual_vals = arr[10:]
```

### Step 5: Call assert_equal()

```python
assert_equal(actual_vals, expected_vals)
```


## Complete Example

```python
# Workflow
arr = np.arange(100)
expected_vals = np.copy(arr[:-10])
arr[10:] = arr[:-10]
actual_vals = arr[10:]
assert_equal(actual_vals, expected_vals)
```

## Next Steps


---

*Source: test_indexing.py:157 | Complexity: Intermediate | Last updated: 2026-06-02*