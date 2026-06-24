# How To: Sort Values Stable Multicolumn Sort

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test sort values stable multicolumn sort

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: expected_idx_non_na, ascending, na_position
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, np.nan, 1, 1, 1, 6, 8, 4, 8, 8, np.nan, np.nan, 8, 8], 'B': [9, np.nan, 5, 2, 2, 2, 5, 4, 5, 3, 4, np.nan, np.nan, 4, 4]})
```

### Step 2: Assign expected_idx = value

```python
expected_idx = [11, 12, 2] + expected_idx_non_na if na_position == 'first' else expected_idx_non_na + [2, 11, 12]
```

### Step 3: Assign expected = df.take(...)

```python
expected = df.take(expected_idx)
```

### Step 4: Assign sorted_df = df.sort_values(...)

```python
sorted_df = df.sort_values(['A', 'B'], ascending=ascending, na_position=na_position)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```


## Complete Example

```python
# Setup
# Fixtures: expected_idx_non_na, ascending, na_position

# Workflow
df = DataFrame({'A': [1, 2, np.nan, 1, 1, 1, 6, 8, 4, 8, 8, np.nan, np.nan, 8, 8], 'B': [9, np.nan, 5, 2, 2, 2, 5, 4, 5, 3, 4, np.nan, np.nan, 4, 4]})
expected_idx = [11, 12, 2] + expected_idx_non_na if na_position == 'first' else expected_idx_non_na + [2, 11, 12]
expected = df.take(expected_idx)
sorted_df = df.sort_values(['A', 'B'], ascending=ascending, na_position=na_position)
tm.assert_frame_equal(sorted_df, expected)
```

## Next Steps


---

*Source: test_sort_values.py:266 | Complexity: Intermediate | Last updated: 2026-06-02*