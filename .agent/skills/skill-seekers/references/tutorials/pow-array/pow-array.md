# How To: Pow Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pow array

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([0, 0, 0, 1, 1, 1, None, None, None])
```

### Step 2: Assign b = pd.array(...)

```python
b = pd.array([0, 1, None, 0, 1, None, 0, 1, None])
```

### Step 3: Assign result = value

```python
result = a ** b
```

### Step 4: Assign expected = pd.array(...)

```python
expected = pd.array([1, 0, None, 1, 1, 1, 1, None, None])
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
a = pd.array([0, 0, 0, 1, 1, 1, None, None, None])
b = pd.array([0, 1, None, 0, 1, None, 0, 1, None])
result = a ** b
expected = pd.array([1, 0, None, 1, 1, 1, 1, None, None])
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:146 | Complexity: Intermediate | Last updated: 2026-06-02*