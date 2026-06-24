# How To: To Array Mixed Integer Float

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to array mixed integer float

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.arrays.floating`


## Step-by-Step Guide

### Step 1: Assign result = pd.array(...)

```python
result = pd.array([1, 2.0])
```

### Step 2: Assign expected = pd.array(...)

```python
expected = pd.array([1.0, 2.0], dtype='Float64')
```

### Step 3: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 4: Assign result = pd.array(...)

```python
result = pd.array([1, None, 2.0])
```

### Step 5: Assign expected = pd.array(...)

```python
expected = pd.array([1.0, None, 2.0], dtype='Float64')
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
result = pd.array([1, 2.0])
expected = pd.array([1.0, 2.0], dtype='Float64')
tm.assert_extension_array_equal(result, expected)
result = pd.array([1, None, 2.0])
expected = pd.array([1.0, None, 2.0], dtype='Float64')
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_construction.py:94 | Complexity: Intermediate | Last updated: 2026-06-02*