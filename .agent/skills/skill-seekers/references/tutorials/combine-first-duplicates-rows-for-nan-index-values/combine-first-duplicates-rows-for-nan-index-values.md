# How To: Combine First Duplicates Rows For Nan Index Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine first duplicates rows for nan index values

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

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'x': [9, 10, 11]}, index=MultiIndex.from_arrays([[1, 2, 3], [np.nan, 5, 6]], names=['a', 'b']))
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'y': [12, 13, 14]}, index=MultiIndex.from_arrays([[1, 2, 4], [np.nan, 5, 7]], names=['a', 'b']))
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'x': [9.0, 10.0, 11.0, np.nan], 'y': [12.0, 13.0, np.nan, 14.0]}, index=MultiIndex.from_arrays([[1, 2, 3, 4], [np.nan, 5, 6, 7]], names=['a', 'b']))
```

### Step 4: Assign combined = df1.combine_first(...)

```python
combined = df1.combine_first(df2)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(combined, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'x': [9, 10, 11]}, index=MultiIndex.from_arrays([[1, 2, 3], [np.nan, 5, 6]], names=['a', 'b']))
df2 = DataFrame({'y': [12, 13, 14]}, index=MultiIndex.from_arrays([[1, 2, 4], [np.nan, 5, 7]], names=['a', 'b']))
expected = DataFrame({'x': [9.0, 10.0, 11.0, np.nan], 'y': [12.0, 13.0, np.nan, 14.0]}, index=MultiIndex.from_arrays([[1, 2, 3, 4], [np.nan, 5, 6, 7]], names=['a', 'b']))
combined = df1.combine_first(df2)
tm.assert_frame_equal(combined, expected)
```

## Next Steps


---

*Source: test_combine_first.py:503 | Complexity: Intermediate | Last updated: 2026-06-02*