# How To: Unary Float Operators

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unary float operators

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
# Fixtures: float_ea_dtype, source, neg_target, abs_target
```

## Step-by-Step Guide

### Step 1: Assign dtype = float_ea_dtype

```python
dtype = float_ea_dtype
```

**Verification:**
```python
assert not tm.shares_memory(pos_result, arr)
```

### Step 2: Assign arr = pd.array(...)

```python
arr = pd.array(source, dtype=dtype)
```

### Step 3: Assign unknown = value

```python
neg_result, pos_result, abs_result = (-arr, +arr, abs(arr))
```

### Step 4: Assign neg_target = pd.array(...)

```python
neg_target = pd.array(neg_target, dtype=dtype)
```

### Step 5: Assign abs_target = pd.array(...)

```python
abs_target = pd.array(abs_target, dtype=dtype)
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(neg_result, neg_target)
```

### Step 7: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(pos_result, arr)
```

**Verification:**
```python
assert not tm.shares_memory(pos_result, arr)
```

### Step 8: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(abs_result, abs_target)
```


## Complete Example

```python
# Setup
# Fixtures: float_ea_dtype, source, neg_target, abs_target

# Workflow
dtype = float_ea_dtype
arr = pd.array(source, dtype=dtype)
neg_result, pos_result, abs_result = (-arr, +arr, abs(arr))
neg_target = pd.array(neg_target, dtype=dtype)
abs_target = pd.array(abs_target, dtype=dtype)
tm.assert_extension_array_equal(neg_result, neg_target)
tm.assert_extension_array_equal(pos_result, arr)
assert not tm.shares_memory(pos_result, arr)
tm.assert_extension_array_equal(abs_result, abs_target)
```

## Next Steps


---

*Source: test_arithmetic.py:217 | Complexity: Advanced | Last updated: 2026-06-02*