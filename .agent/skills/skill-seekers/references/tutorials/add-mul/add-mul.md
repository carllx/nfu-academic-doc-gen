# How To: Add Mul

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test add mul

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
# Fixtures: dtype, opname, exp
```

## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([0, 1, None, 3, 4], dtype=dtype)
```

### Step 2: Assign b = pd.array(...)

```python
b = pd.array([1, 2, 3, None, 5], dtype=dtype)
```

### Step 3: Assign expected = pd.array(...)

```python
expected = pd.array(exp, dtype=dtype)
```

### Step 4: Assign op = getattr(...)

```python
op = getattr(operator, opname)
```

### Step 5: Assign result = op(...)

```python
result = op(a, b)
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 7: Assign op = getattr(...)

```python
op = getattr(ops, 'r' + opname)
```

### Step 8: Assign result = op(...)

```python
result = op(a, b)
```

### Step 9: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, opname, exp

# Workflow
a = pd.array([0, 1, None, 3, 4], dtype=dtype)
b = pd.array([1, 2, 3, None, 5], dtype=dtype)
expected = pd.array(exp, dtype=dtype)
op = getattr(operator, opname)
result = op(a, b)
tm.assert_extension_array_equal(result, expected)
op = getattr(ops, 'r' + opname)
result = op(a, b)
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:20 | Complexity: Advanced | Last updated: 2026-06-02*