# How To: Rank Empty Group

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rank empty group

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign column = 'A'

```python
column = 'A'
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [0, 1, 0], 'B': [1.0, np.nan, 2.0]})
```

### Step 3: Assign result = df.groupby.B.rank(...)

```python
result = df.groupby(column).B.rank(pct=True)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([0.5, np.nan, 1.0], name='B')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = df.groupby.rank(...)

```python
result = df.groupby(column).rank(pct=True)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'B': [0.5, np.nan, 1.0]})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
column = 'A'
df = DataFrame({'A': [0, 1, 0], 'B': [1.0, np.nan, 2.0]})
result = df.groupby(column).B.rank(pct=True)
expected = Series([0.5, np.nan, 1.0], name='B')
tm.assert_series_equal(result, expected)
result = df.groupby(column).rank(pct=True)
expected = DataFrame({'B': [0.5, np.nan, 1.0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_rank.py:533 | Complexity: Advanced | Last updated: 2026-06-02*