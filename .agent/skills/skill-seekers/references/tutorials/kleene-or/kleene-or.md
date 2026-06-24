# How To: Kleene Or

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test kleene or

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `pandas.core.ops.mask_ops`
- `pandas.tests.extension.base`


## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([True] * 3 + [False] * 3 + [None] * 3, dtype='boolean')
```

### Step 2: Assign b = pd.array(...)

```python
b = pd.array([True, False, None] * 3, dtype='boolean')
```

### Step 3: Assign result = value

```python
result = a | b
```

### Step 4: Assign expected = pd.array(...)

```python
expected = pd.array([True, True, True, True, False, None, True, None, None], dtype='boolean')
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = b | a
```

### Step 7: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 8: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(a, pd.array([True] * 3 + [False] * 3 + [None] * 3, dtype='boolean'))
```

### Step 9: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(b, pd.array([True, False, None] * 3, dtype='boolean'))
```


## Complete Example

```python
# Workflow
a = pd.array([True] * 3 + [False] * 3 + [None] * 3, dtype='boolean')
b = pd.array([True, False, None] * 3, dtype='boolean')
result = a | b
expected = pd.array([True, True, True, True, False, None, True, None, None], dtype='boolean')
tm.assert_extension_array_equal(result, expected)
result = b | a
tm.assert_extension_array_equal(result, expected)
tm.assert_extension_array_equal(a, pd.array([True] * 3 + [False] * 3 + [None] * 3, dtype='boolean'))
tm.assert_extension_array_equal(b, pd.array([True, False, None] * 3, dtype='boolean'))
```

## Next Steps


---

*Source: test_logical.py:91 | Complexity: Advanced | Last updated: 2026-06-02*