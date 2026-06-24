# How To: Append Different Columns Types

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test append different columns types

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: df_columns, series_index
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=df_columns)
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([7, 8, 9], index=series_index, name=2)
```

### Step 3: Assign result = df._append(...)

```python
result = df._append(ser)
```

### Step 4: Assign idx_diff = ser.index.difference(...)

```python
idx_diff = ser.index.difference(df_columns)
```

### Step 5: Assign combined_columns = Index.append(...)

```python
combined_columns = Index(df_columns.tolist()).append(idx_diff)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1.0, 2.0, 3.0, np.nan, np.nan, np.nan], [4, 5, 6, np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan, 7, 8, 9]], index=[0, 1, 2], columns=combined_columns)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: df_columns, series_index

# Workflow
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=df_columns)
ser = Series([7, 8, 9], index=series_index, name=2)
result = df._append(ser)
idx_diff = ser.index.difference(df_columns)
combined_columns = Index(df_columns.tolist()).append(idx_diff)
expected = DataFrame([[1.0, 2.0, 3.0, np.nan, np.nan, np.nan], [4, 5, 6, np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan, 7, 8, 9]], index=[0, 1, 2], columns=combined_columns)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_append.py:226 | Complexity: Intermediate | Last updated: 2026-06-02*