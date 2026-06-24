# How To: Array Equivalent Nested Mixed List

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test array equivalent nested mixed list

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: strict_nan
```

## Step-by-Step Guide

### Step 1: Assign left = np.array(...)

```python
left = np.array([np.array([1, 2, 3]), np.array([4, 5])], dtype=object)
```

**Verification:**
```python
assert array_equivalent(left, right, strict_nan=strict_nan)
```

### Step 2: Assign right = np.array(...)

```python
right = np.array([[1, 2, 3], [4, 5]], dtype=object)
```

**Verification:**
```python
assert not array_equivalent(left, right[::-1], strict_nan=strict_nan)
```

### Step 3: Assign left = np.array(...)

```python
left = np.array([np.array([np.array([1, 2, 3]), np.array([4, 5])], dtype=object), np.array([np.array([6]), np.array([7, 8]), np.array([9])], dtype=object)], dtype=object)
```

**Verification:**
```python
assert array_equivalent(left, right, strict_nan=strict_nan)
```

### Step 4: Assign right = np.array(...)

```python
right = np.array([[[1, 2, 3], [4, 5]], [[6], [7, 8], [9]]], dtype=object)
```

**Verification:**
```python
assert not array_equivalent(left, right[::-1], strict_nan=strict_nan)
```

### Step 5: Assign subarr = np.empty(...)

```python
subarr = np.empty(2, dtype=object)
```

**Verification:**
```python
assert array_equivalent(left, right, strict_nan=strict_nan)
```

### Step 6: Assign unknown = value

```python
subarr[:] = [np.array([None, 'b'], dtype=object), np.array(['c', 'd'], dtype=object)]
```

**Verification:**
```python
assert not array_equivalent(left, right[::-1], strict_nan=strict_nan)
```

### Step 7: Assign left = np.array(...)

```python
left = np.array([subarr, None], dtype=object)
```

### Step 8: Assign right = np.array(...)

```python
right = np.array([[[None, 'b'], ['c', 'd']], None], dtype=object)
```

**Verification:**
```python
assert array_equivalent(left, right, strict_nan=strict_nan)
```


## Complete Example

```python
# Setup
# Fixtures: strict_nan

# Workflow
left = np.array([np.array([1, 2, 3]), np.array([4, 5])], dtype=object)
right = np.array([[1, 2, 3], [4, 5]], dtype=object)
assert array_equivalent(left, right, strict_nan=strict_nan)
assert not array_equivalent(left, right[::-1], strict_nan=strict_nan)
left = np.array([np.array([np.array([1, 2, 3]), np.array([4, 5])], dtype=object), np.array([np.array([6]), np.array([7, 8]), np.array([9])], dtype=object)], dtype=object)
right = np.array([[[1, 2, 3], [4, 5]], [[6], [7, 8], [9]]], dtype=object)
assert array_equivalent(left, right, strict_nan=strict_nan)
assert not array_equivalent(left, right[::-1], strict_nan=strict_nan)
subarr = np.empty(2, dtype=object)
subarr[:] = [np.array([None, 'b'], dtype=object), np.array(['c', 'd'], dtype=object)]
left = np.array([subarr, None], dtype=object)
right = np.array([[[None, 'b'], ['c', 'd']], None], dtype=object)
assert array_equivalent(left, right, strict_nan=strict_nan)
assert not array_equivalent(left, right[::-1], strict_nan=strict_nan)
```

## Next Steps


---

*Source: test_missing.py:640 | Complexity: Advanced | Last updated: 2026-06-02*