# How To: Partial Set Empty Frame5

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test partial set empty frame5

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame()
```

### Step 2: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.columns, pd.RangeIndex(0))
```

### Step 3: Assign df2 = DataFrame(...)

```python
df2 = DataFrame()
```

### Step 4: Assign unknown = Series(...)

```python
df2[1] = Series([1], index=['foo'])
```

### Step 5: Assign unknown = Series(...)

```python
df.loc[:, 1] = Series([1], index=['foo'])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, DataFrame([[1]], index=['foo'], columns=[1]))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df2)
```


## Complete Example

```python
# Workflow
df = DataFrame()
tm.assert_index_equal(df.columns, pd.RangeIndex(0))
df2 = DataFrame()
df2[1] = Series([1], index=['foo'])
df.loc[:, 1] = Series([1], index=['foo'])
tm.assert_frame_equal(df, DataFrame([[1]], index=['foo'], columns=[1]))
tm.assert_frame_equal(df, df2)
```

## Next Steps


---

*Source: test_partial.py:139 | Complexity: Intermediate | Last updated: 2026-06-02*