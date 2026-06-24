# How To: Join Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test join dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_numeric_ea_dtype, val
```

## Step-by-Step Guide

### Step 1: Assign midx = MultiIndex.from_arrays(...)

```python
midx = MultiIndex.from_arrays([Series([1, 2], dtype=any_numeric_ea_dtype), [3, 4]])
```

### Step 2: Assign midx2 = MultiIndex.from_arrays(...)

```python
midx2 = MultiIndex.from_arrays([Series([1, val, val], dtype=any_numeric_ea_dtype), [3, 4, 4]])
```

### Step 3: Assign result = midx.join(...)

```python
result = midx.join(midx2, how='outer')
```

### Step 4: Assign expected = MultiIndex.from_arrays.sort_values(...)

```python
expected = MultiIndex.from_arrays([Series([val, val, 1, 2], dtype=any_numeric_ea_dtype), [4, 4, 3, 4]]).sort_values()
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_numeric_ea_dtype, val

# Workflow
midx = MultiIndex.from_arrays([Series([1, 2], dtype=any_numeric_ea_dtype), [3, 4]])
midx2 = MultiIndex.from_arrays([Series([1, val, val], dtype=any_numeric_ea_dtype), [3, 4, 4]])
result = midx.join(midx2, how='outer')
expected = MultiIndex.from_arrays([Series([val, val, 1, 2], dtype=any_numeric_ea_dtype), [4, 4, 3, 4]]).sort_values()
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:228 | Complexity: Intermediate | Last updated: 2026-06-02*