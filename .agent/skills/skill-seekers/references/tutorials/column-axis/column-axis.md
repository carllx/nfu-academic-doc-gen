# How To: Column Axis

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test column axis

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: column_group_df
```

## Step-by-Step Guide

### Step 1: Assign msg = 'DataFrame.groupby with axis=1'

```python
msg = 'DataFrame.groupby with axis=1'
```

### Step 2: Assign result = value

```python
result = g._positional_selector[1:-1]
```

### Step 3: Assign expected = value

```python
expected = column_group_df.iloc[:, [1, 3]]
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign g = column_group_df.groupby(...)

```python
g = column_group_df.groupby(column_group_df.iloc[1], axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: column_group_df

# Workflow
msg = 'DataFrame.groupby with axis=1'
with tm.assert_produces_warning(FutureWarning, match=msg):
    g = column_group_df.groupby(column_group_df.iloc[1], axis=1)
result = g._positional_selector[1:-1]
expected = column_group_df.iloc[:, [1, 3]]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:282 | Complexity: Intermediate | Last updated: 2026-06-02*