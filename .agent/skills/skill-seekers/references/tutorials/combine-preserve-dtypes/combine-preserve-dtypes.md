# How To: Combine Preserve Dtypes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine preserve dtypes

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

### Step 1: Assign a_column = Series(...)

```python
a_column = Series(['a', 'b'], index=range(2))
```

### Step 2: Assign b_column = Series(...)

```python
b_column = Series(range(2), index=range(2))
```

### Step 3: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'A': a_column, 'B': b_column})
```

### Step 4: Assign c_column = Series(...)

```python
c_column = Series(['a', 'b'], index=range(5, 7))
```

### Step 5: Assign b_column = Series(...)

```python
b_column = Series(range(-1, 1), index=range(5, 7))
```

### Step 6: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'B': b_column, 'C': c_column})
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': ['a', 'b', np.nan, np.nan], 'B': [0, 1, -1, 0], 'C': [np.nan, np.nan, 'a', 'b']}, index=[0, 1, 5, 6])
```

### Step 8: Assign combined = df1.combine_first(...)

```python
combined = df1.combine_first(df2)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(combined, expected)
```


## Complete Example

```python
# Workflow
a_column = Series(['a', 'b'], index=range(2))
b_column = Series(range(2), index=range(2))
df1 = DataFrame({'A': a_column, 'B': b_column})
c_column = Series(['a', 'b'], index=range(5, 7))
b_column = Series(range(-1, 1), index=range(5, 7))
df2 = DataFrame({'B': b_column, 'C': c_column})
expected = DataFrame({'A': ['a', 'b', np.nan, np.nan], 'B': [0, 1, -1, 0], 'C': [np.nan, np.nan, 'a', 'b']}, index=[0, 1, 5, 6])
combined = df1.combine_first(df2)
tm.assert_frame_equal(combined, expected)
```

## Next Steps


---

*Source: test_combine_first.py:481 | Complexity: Advanced | Last updated: 2026-06-02*