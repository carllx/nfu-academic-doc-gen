# How To: Negative Difference

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Check correct behavior of unsigned dtypes if there is a negative
difference between the edge to pad and `end_values`. Check both cases
to be independent of implementation. Test behavior for all other dtypes
in case dtype casting interferes with complex dtypes. See gh-14191.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.lib._arraypad_impl`
- `numpy.testing`
- `fractions`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: '\n        Check correct behavior of unsigned dtypes if there is a negative\n        difference between the edge to pad and `end_values`. Check both cases\n        to be independent of implementation. Test behavior for all other dtypes\n        in case dtype casting interferes with complex dtypes. See gh-14191.\n        '

```python
'\n        Check correct behavior of unsigned dtypes if there is a negative\n        difference between the edge to pad and `end_values`. Check both cases\n        to be independent of implementation. Test behavior for all other dtypes\n        in case dtype casting interferes with complex dtypes. See gh-14191.\n        '
```

**Verification:**
```python
assert_equal(result, expected)
```

### Step 2: Assign x = np.array(...)

```python
x = np.array([3], dtype=dtype)
```

**Verification:**
```python
assert_equal(result, expected)
```

### Step 3: Assign result = np.pad(...)

```python
result = np.pad(x, 3, mode='linear_ramp', end_values=0)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([0, 1, 2, 3, 2, 1, 0], dtype=dtype)
```

### Step 5: Call assert_equal()

```python
assert_equal(result, expected)
```

### Step 6: Assign x = np.array(...)

```python
x = np.array([0], dtype=dtype)
```

### Step 7: Assign result = np.pad(...)

```python
result = np.pad(x, 3, mode='linear_ramp', end_values=3)
```

### Step 8: Assign expected = np.array(...)

```python
expected = np.array([3, 2, 1, 0, 1, 2, 3], dtype=dtype)
```

### Step 9: Call assert_equal()

```python
assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
'\n        Check correct behavior of unsigned dtypes if there is a negative\n        difference between the edge to pad and `end_values`. Check both cases\n        to be independent of implementation. Test behavior for all other dtypes\n        in case dtype casting interferes with complex dtypes. See gh-14191.\n        '
x = np.array([3], dtype=dtype)
result = np.pad(x, 3, mode='linear_ramp', end_values=0)
expected = np.array([0, 1, 2, 3, 2, 1, 0], dtype=dtype)
assert_equal(result, expected)
x = np.array([0], dtype=dtype)
result = np.pad(x, 3, mode='linear_ramp', end_values=3)
expected = np.array([3, 2, 1, 0, 1, 2, 3], dtype=dtype)
assert_equal(result, expected)
```

## Next Steps


---

*Source: test_arraypad.py:743 | Complexity: Advanced | Last updated: 2026-06-02*