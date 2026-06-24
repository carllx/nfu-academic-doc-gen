# How To: Putmask Keep Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test putmask keep dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_numeric_ea_dtype
```

## Step-by-Step Guide

### Step 1: Assign midx = MultiIndex.from_arrays(...)

```python
midx = MultiIndex.from_arrays([pd.Series([1, 2, 3], dtype=any_numeric_ea_dtype), [10, 11, 12]])
```

### Step 2: Assign midx2 = MultiIndex.from_arrays(...)

```python
midx2 = MultiIndex.from_arrays([pd.Series([5, 6, 7], dtype=any_numeric_ea_dtype), [-1, -2, -3]])
```

### Step 3: Assign result = midx.putmask(...)

```python
result = midx.putmask([True, False, False], midx2)
```

### Step 4: Assign expected = MultiIndex.from_arrays(...)

```python
expected = MultiIndex.from_arrays([pd.Series([5, 2, 3], dtype=any_numeric_ea_dtype), [-1, 11, 12]])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_numeric_ea_dtype

# Workflow
midx = MultiIndex.from_arrays([pd.Series([1, 2, 3], dtype=any_numeric_ea_dtype), [10, 11, 12]])
midx2 = MultiIndex.from_arrays([pd.Series([5, 6, 7], dtype=any_numeric_ea_dtype), [-1, -2, -3]])
result = midx.putmask([True, False, False], midx2)
expected = MultiIndex.from_arrays([pd.Series([5, 2, 3], dtype=any_numeric_ea_dtype), [-1, 11, 12]])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:179 | Complexity: Intermediate | Last updated: 2026-06-02*