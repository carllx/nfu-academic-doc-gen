# How To: Midx Losing Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test midx losing dtype

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign midx = MultiIndex.from_arrays(...)

```python
midx = MultiIndex.from_arrays([[0, 0], [np.nan, np.nan]])
```

### Step 2: Assign midx2 = MultiIndex.from_arrays(...)

```python
midx2 = MultiIndex.from_arrays([[1, 1], [np.nan, np.nan]])
```

### Step 3: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'a': [None, 4]}, index=midx)
```

### Step 4: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'a': [3, 3]}, index=midx2)
```

### Step 5: Assign result = df1.combine_first(...)

```python
result = df1.combine_first(df2)
```

### Step 6: Assign expected_midx = MultiIndex.from_arrays(...)

```python
expected_midx = MultiIndex.from_arrays([[0, 0, 1, 1], [np.nan, np.nan, np.nan, np.nan]])
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [np.nan, 4, 3, 3]}, index=expected_midx)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
midx = MultiIndex.from_arrays([[0, 0], [np.nan, np.nan]])
midx2 = MultiIndex.from_arrays([[1, 1], [np.nan, np.nan]])
df1 = DataFrame({'a': [None, 4]}, index=midx)
df2 = DataFrame({'a': [3, 3]}, index=midx2)
result = df1.combine_first(df2)
expected_midx = MultiIndex.from_arrays([[0, 0, 1, 1], [np.nan, np.nan, np.nan, np.nan]])
expected = DataFrame({'a': [np.nan, 4, 3, 3]}, index=expected_midx)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_combine_first.py:537 | Complexity: Advanced | Last updated: 2026-06-02*