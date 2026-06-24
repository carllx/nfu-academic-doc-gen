# How To: Div

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test div

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([1, 2, 3, None, 5], dtype=dtype)
```

### Step 2: Assign b = pd.array(...)

```python
b = pd.array([0, 1, None, 3, 4], dtype=dtype)
```

### Step 3: Assign result = value

```python
result = a / b
```

### Step 4: Assign expected = pd.array(...)

```python
expected = pd.array([np.inf, 2, None, None, 1.25], dtype='Float64')
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
a = pd.array([1, 2, 3, None, 5], dtype=dtype)
b = pd.array([0, 1, None, 3, 4], dtype=dtype)
result = a / b
expected = pd.array([np.inf, 2, None, None, 1.25], dtype='Float64')
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:45 | Complexity: Intermediate | Last updated: 2026-06-02*