# How To: Combine First Int64 Not Cast To Float64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine first int64 not cast to float64

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

### Step 1: Assign df_1 = DataFrame(...)

```python
df_1 = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
```

### Step 2: Assign df_2 = DataFrame(...)

```python
df_2 = DataFrame({'A': [1, 20, 30], 'B': [40, 50, 60], 'C': [12, 34, 65]})
```

### Step 3: Assign result = df_1.combine_first(...)

```python
result = df_1.combine_first(df_2)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [12, 34, 65]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df_1 = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df_2 = DataFrame({'A': [1, 20, 30], 'B': [40, 50, 60], 'C': [12, 34, 65]})
result = df_1.combine_first(df_2)
expected = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [12, 34, 65]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_combine_first.py:528 | Complexity: Intermediate | Last updated: 2026-06-02*