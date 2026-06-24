# How To: Divmod Array

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test divmod array

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.tests.extension`
- `pandas.tests.extension.decimal.array`

**Setup Required:**
```python
# Fixtures: reverse, expected_div, expected_mod
```

## Step-by-Step Guide

### Step 1: Assign arr = to_decimal(...)

```python
arr = to_decimal([1, 2, 3, 4])
```

### Step 2: Assign expected_div = to_decimal(...)

```python
expected_div = to_decimal(expected_div)
```

### Step 3: Assign expected_mod = to_decimal(...)

```python
expected_mod = to_decimal(expected_mod)
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(div, expected_div)
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(mod, expected_mod)
```

### Step 6: Assign unknown = divmod(...)

```python
div, mod = divmod(2, arr)
```

### Step 7: Assign unknown = divmod(...)

```python
div, mod = divmod(arr, 2)
```


## Complete Example

```python
# Setup
# Fixtures: reverse, expected_div, expected_mod

# Workflow
arr = to_decimal([1, 2, 3, 4])
if reverse:
    div, mod = divmod(2, arr)
else:
    div, mod = divmod(arr, 2)
expected_div = to_decimal(expected_div)
expected_mod = to_decimal(expected_mod)
tm.assert_extension_array_equal(div, expected_div)
tm.assert_extension_array_equal(mod, expected_mod)
```

## Next Steps


---

*Source: test_decimal.py:433 | Complexity: Intermediate | Last updated: 2026-06-02*