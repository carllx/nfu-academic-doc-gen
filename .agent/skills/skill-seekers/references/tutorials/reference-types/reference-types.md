# How To: Reference Types

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reference types

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy._core._rational_tests`
- `numpy.lib._stride_tricks_impl`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign input_array = np.array(...)

```python
input_array = np.array('a', dtype=object)
```

**Verification:**
```python
assert_array_equal(expected, actual)
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array(['a'] * 3, dtype=object)
```

**Verification:**
```python
assert_array_equal(expected, actual)
```

### Step 3: Assign actual = broadcast_to(...)

```python
actual = broadcast_to(input_array, (3,))
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(expected, actual)
```

### Step 5: Assign unknown = broadcast_arrays(...)

```python
actual, _ = broadcast_arrays(input_array, np.ones(3))
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(expected, actual)
```


## Complete Example

```python
# Workflow
input_array = np.array('a', dtype=object)
expected = np.array(['a'] * 3, dtype=object)
actual = broadcast_to(input_array, (3,))
assert_array_equal(expected, actual)
actual, _ = broadcast_arrays(input_array, np.ones(3))
assert_array_equal(expected, actual)
```

## Next Steps


---

*Source: test_stride_tricks.py:648 | Complexity: Intermediate | Last updated: 2026-06-02*