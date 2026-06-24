# How To: Compare With Integerarray

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare with integerarray

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.arrays.masked_shared`

**Setup Required:**
```python
# Fixtures: comparison_op
```

## Step-by-Step Guide

### Step 1: Assign op = comparison_op

```python
op = comparison_op
```

### Step 2: Assign a = pd.array(...)

```python
a = pd.array([0, 1, None] * 3, dtype='Int64')
```

### Step 3: Assign b = pd.array(...)

```python
b = pd.array([0] * 3 + [1] * 3 + [None] * 3, dtype='Float64')
```

### Step 4: Assign other = b.astype(...)

```python
other = b.astype('Int64')
```

### Step 5: Assign expected = op(...)

```python
expected = op(a, other)
```

### Step 6: Assign result = op(...)

```python
result = op(a, b)
```

### Step 7: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 8: Assign expected = op(...)

```python
expected = op(other, a)
```

### Step 9: Assign result = op(...)

```python
result = op(b, a)
```

### Step 10: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: comparison_op

# Workflow
op = comparison_op
a = pd.array([0, 1, None] * 3, dtype='Int64')
b = pd.array([0] * 3 + [1] * 3 + [None] * 3, dtype='Float64')
other = b.astype('Int64')
expected = op(a, other)
result = op(a, b)
tm.assert_extension_array_equal(result, expected)
expected = op(other, a)
result = op(b, a)
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_comparison.py:18 | Complexity: Advanced | Last updated: 2026-06-02*