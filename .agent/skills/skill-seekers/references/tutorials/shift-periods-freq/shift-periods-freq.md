# How To: Shift Periods Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shift periods freq

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = {'a': [1, 2, 3, 4, 5, 6], 'b': [0, 0, 0, 1, 1, 1]}
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(data, index=date_range(start='20100101', periods=6))
```

### Step 3: Assign result = df.groupby.shift(...)

```python
result = df.groupby(df.index).shift(periods=-2, freq='D')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(data, index=date_range(start='2009-12-30', periods=6))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = {'a': [1, 2, 3, 4, 5, 6], 'b': [0, 0, 0, 1, 1, 1]}
df = DataFrame(data, index=date_range(start='20100101', periods=6))
result = df.groupby(df.index).shift(periods=-2, freq='D')
expected = DataFrame(data, index=date_range(start='2009-12-30', periods=6))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby_shift_diff.py:161 | Complexity: Intermediate | Last updated: 2026-06-02*