# How To: Cut Out Of Bounds

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cut out of bounds

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape.tile`


## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.standard_normal(...)

```python
arr = np.random.default_rng(2).standard_normal(100)
```

### Step 2: Assign result = cut(...)

```python
result = cut(arr, [-1, 0, 1])
```

### Step 3: Assign mask = isna(...)

```python
mask = isna(result)
```

### Step 4: Assign ex_mask = value

```python
ex_mask = (arr < -1) | (arr > 1)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(mask, ex_mask)
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).standard_normal(100)
result = cut(arr, [-1, 0, 1])
mask = isna(result)
ex_mask = (arr < -1) | (arr > 1)
tm.assert_numpy_array_equal(mask, ex_mask)
```

## Next Steps


---

*Source: test_cut.py:285 | Complexity: Intermediate | Last updated: 2026-06-02*