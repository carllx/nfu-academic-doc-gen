# How To: Setattr Columns Vs Construct With Columns Datetimeindx

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setattr columns vs construct with columns datetimeindx

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('20130101', periods=4, freq='QE-NOV')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 1, 1, 5], [1, 1, 2, 5], [2, 1, 3, 5]], columns=['a', 'a', 'a', 'a'])
```

### Step 3: Assign df.columns = idx

```python
df.columns = idx
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 1, 1, 5], [1, 1, 2, 5], [2, 1, 3, 5]], columns=idx)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
idx = date_range('20130101', periods=4, freq='QE-NOV')
df = DataFrame([[1, 1, 1, 5], [1, 1, 2, 5], [2, 1, 3, 5]], columns=['a', 'a', 'a', 'a'])
df.columns = idx
expected = DataFrame([[1, 1, 1, 5], [1, 1, 2, 5], [2, 1, 3, 5]], columns=idx)
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_nonunique_indexes.py:24 | Complexity: Intermediate | Last updated: 2026-06-02*