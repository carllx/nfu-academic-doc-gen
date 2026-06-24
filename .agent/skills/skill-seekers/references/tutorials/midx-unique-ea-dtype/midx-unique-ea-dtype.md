# How To: Midx Unique Ea Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test midx unique ea dtype

## Prerequisites

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign vals_a = Series(...)

```python
vals_a = Series([1, 2, NA, NA], dtype='Int64')
```

### Step 2: Assign vals_b = np.array(...)

```python
vals_b = np.array([1, 2, 3, 3])
```

### Step 3: Assign midx = MultiIndex.from_arrays(...)

```python
midx = MultiIndex.from_arrays([vals_a, vals_b], names=['a', 'b'])
```

### Step 4: Assign result = midx.unique(...)

```python
result = midx.unique()
```

### Step 5: Assign exp_vals_a = Series(...)

```python
exp_vals_a = Series([1, 2, NA], dtype='Int64')
```

### Step 6: Assign exp_vals_b = np.array(...)

```python
exp_vals_b = np.array([1, 2, 3])
```

### Step 7: Assign expected = MultiIndex.from_arrays(...)

```python
expected = MultiIndex.from_arrays([exp_vals_a, exp_vals_b], names=['a', 'b'])
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
vals_a = Series([1, 2, NA, NA], dtype='Int64')
vals_b = np.array([1, 2, 3, 3])
midx = MultiIndex.from_arrays([vals_a, vals_b], names=['a', 'b'])
result = midx.unique()
exp_vals_a = Series([1, 2, NA], dtype='Int64')
exp_vals_b = np.array([1, 2, 3])
expected = MultiIndex.from_arrays([exp_vals_a, exp_vals_b], names=['a', 'b'])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_duplicates.py:353 | Complexity: Advanced | Last updated: 2026-06-02*