# How To: Astype Str Int Categories To Nullable Int

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype str int categories to nullable int

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dtype = CategoricalDtype(...)

```python
dtype = CategoricalDtype([str(i) for i in range(5)])
```

### Step 2: Assign codes = np.random.default_rng.integers(...)

```python
codes = np.random.default_rng(2).integers(5, size=20)
```

### Step 3: Assign arr = Categorical.from_codes(...)

```python
arr = Categorical.from_codes(codes, dtype=dtype)
```

### Step 4: Assign res = arr.astype(...)

```python
res = arr.astype('Int64')
```

### Step 5: Assign expected = array(...)

```python
expected = array(codes, dtype='Int64')
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(res, expected)
```


## Complete Example

```python
# Workflow
dtype = CategoricalDtype([str(i) for i in range(5)])
codes = np.random.default_rng(2).integers(5, size=20)
arr = Categorical.from_codes(codes, dtype=dtype)
res = arr.astype('Int64')
expected = array(codes, dtype='Int64')
tm.assert_extension_array_equal(res, expected)
```

## Next Steps


---

*Source: test_astype.py:64 | Complexity: Intermediate | Last updated: 2026-06-02*