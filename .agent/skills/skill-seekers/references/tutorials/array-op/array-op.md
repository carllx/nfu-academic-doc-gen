# How To: Array Op

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test array op

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: dtype, opname, exp
```

## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([1.0, 2.0, None, 4.0, 5.0], dtype=dtype)
```

### Step 2: Assign b = pd.array(...)

```python
b = pd.array([0.1, 0.2, 0.3, None, 0.5], dtype=dtype)
```

### Step 3: Assign op = getattr(...)

```python
op = getattr(operator, opname)
```

### Step 4: Assign result = op(...)

```python
result = op(a, b)
```

### Step 5: Assign expected = pd.array(...)

```python
expected = pd.array(exp, dtype=dtype)
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, opname, exp

# Workflow
a = pd.array([1.0, 2.0, None, 4.0, 5.0], dtype=dtype)
b = pd.array([0.1, 0.2, 0.3, None, 0.5], dtype=dtype)
op = getattr(operator, opname)
result = op(a, b)
expected = pd.array(exp, dtype=dtype)
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:26 | Complexity: Intermediate | Last updated: 2026-06-02*