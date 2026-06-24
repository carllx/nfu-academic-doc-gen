# How To: Empty Ok

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty ok

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `pandas.core.ops.mask_ops`
- `pandas.tests.extension.base`

**Setup Required:**
```python
# Fixtures: all_logical_operators
```

## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([], dtype='boolean')
```

### Step 2: Assign op_name = all_logical_operators

```python
op_name = all_logical_operators
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(a, op_name)(True)
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(a, result)
```

### Step 5: Assign result = getattr(...)

```python
result = getattr(a, op_name)(False)
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(a, result)
```

### Step 7: Assign result = getattr(...)

```python
result = getattr(a, op_name)(pd.NA)
```

### Step 8: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(a, result)
```


## Complete Example

```python
# Setup
# Fixtures: all_logical_operators

# Workflow
a = pd.array([], dtype='boolean')
op_name = all_logical_operators
result = getattr(a, op_name)(True)
tm.assert_extension_array_equal(a, result)
result = getattr(a, op_name)(False)
tm.assert_extension_array_equal(a, result)
result = getattr(a, op_name)(pd.NA)
tm.assert_extension_array_equal(a, result)
```

## Next Steps


---

*Source: test_logical.py:37 | Complexity: Advanced | Last updated: 2026-06-02*