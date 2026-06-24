# How To: To Boolean Array From Integer Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to boolean array from integer array

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `pandas.core.arrays.boolean`


## Step-by-Step Guide

### Step 1: Assign result = pd.array(...)

```python
result = pd.array(np.array([1, 0, 1, 0]), dtype='boolean')
```

### Step 2: Assign expected = pd.array(...)

```python
expected = pd.array([True, False, True, False], dtype='boolean')
```

### Step 3: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 4: Assign result = pd.array(...)

```python
result = pd.array(np.array([1, 0, 1, None]), dtype='boolean')
```

### Step 5: Assign expected = pd.array(...)

```python
expected = pd.array([True, False, True, None], dtype='boolean')
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
result = pd.array(np.array([1, 0, 1, 0]), dtype='boolean')
expected = pd.array([True, False, True, False], dtype='boolean')
tm.assert_extension_array_equal(result, expected)
result = pd.array(np.array([1, 0, 1, None]), dtype='boolean')
expected = pd.array([True, False, True, None], dtype='boolean')
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_construction.py:120 | Complexity: Intermediate | Last updated: 2026-06-02*