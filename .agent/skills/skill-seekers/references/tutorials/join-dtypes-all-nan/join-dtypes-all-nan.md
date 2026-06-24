# How To: Join Dtypes All Nan

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join dtypes all nan

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_numeric_ea_dtype
```

## Step-by-Step Guide

### Step 1: Assign midx = MultiIndex.from_arrays(...)

```python
midx = MultiIndex.from_arrays([Series([1, 2], dtype=any_numeric_ea_dtype), [np.nan, np.nan]])
```

### Step 2: Assign midx2 = MultiIndex.from_arrays(...)

```python
midx2 = MultiIndex.from_arrays([Series([1, 0, 0], dtype=any_numeric_ea_dtype), [np.nan, np.nan, np.nan]])
```

### Step 3: Assign result = midx.join(...)

```python
result = midx.join(midx2, how='outer')
```

### Step 4: Assign expected = MultiIndex.from_arrays(...)

```python
expected = MultiIndex.from_arrays([Series([0, 0, 1, 2], dtype=any_numeric_ea_dtype), [np.nan, np.nan, np.nan, np.nan]])
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
midx = MultiIndex.from_arrays([Series([1, 2], dtype=any_numeric_ea_dtype), [np.nan, np.nan]])
midx2 = MultiIndex.from_arrays([Series([1, 0, 0], dtype=any_numeric_ea_dtype), [np.nan, np.nan, np.nan]])
result = midx.join(midx2, how='outer')
expected = MultiIndex.from_arrays([Series([0, 0, 1, 2], dtype=any_numeric_ea_dtype), [np.nan, np.nan, np.nan, np.nan]])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:241 | Complexity: Intermediate | Last updated: 2026-06-02*