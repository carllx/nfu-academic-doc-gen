# How To: Combine First Timestamp Bug Nat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine first timestamp bug NaT

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

### Step 1: Assign frame = DataFrame(...)

```python
frame = DataFrame([[pd.NaT, pd.NaT]], columns=['a', 'b'])
```

### Step 2: Assign other = DataFrame(...)

```python
other = DataFrame([[datetime(2020, 1, 1), datetime(2020, 1, 2)]], columns=['b', 'c'])
```

### Step 3: Assign result = frame.combine_first(...)

```python
result = frame.combine_first(other)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[pd.NaT, datetime(2020, 1, 1), datetime(2020, 1, 2)]], columns=['a', 'b', 'c'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
frame = DataFrame([[pd.NaT, pd.NaT]], columns=['a', 'b'])
other = DataFrame([[datetime(2020, 1, 1), datetime(2020, 1, 2)]], columns=['b', 'c'])
result = frame.combine_first(other)
expected = DataFrame([[pd.NaT, datetime(2020, 1, 1), datetime(2020, 1, 2)]], columns=['a', 'b', 'c'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_combine_first.py:437 | Complexity: Intermediate | Last updated: 2026-06-02*