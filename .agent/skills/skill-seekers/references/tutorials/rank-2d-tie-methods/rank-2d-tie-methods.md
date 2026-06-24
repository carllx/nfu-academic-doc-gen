# How To: Rank 2D Tie Methods

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rank 2d tie methods

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.algos`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method, axis, dtype
```

## Step-by-Step Guide

### Step 1: Assign df = value

```python
df = self.df
```

### Step 2: Assign frame = value

```python
frame = df if dtype is None else df.astype(dtype)
```

### Step 3: Call _check2d()

```python
_check2d(frame, self.results[method], method=method, axis=axis)
```

### Step 4: Assign exp_df = DataFrame(...)

```python
exp_df = DataFrame({'A': expected, 'B': expected})
```

### Step 5: Assign result = df.rank(...)

```python
result = df.rank(method=method, axis=axis)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, exp_df)
```

### Step 7: Assign df = value

```python
df = df.T
```

### Step 8: Assign exp_df = value

```python
exp_df = exp_df.T
```


## Complete Example

```python
# Setup
# Fixtures: method, axis, dtype

# Workflow
df = self.df

def _check2d(df, expected, method='average', axis=0):
    exp_df = DataFrame({'A': expected, 'B': expected})
    if axis == 1:
        df = df.T
        exp_df = exp_df.T
    result = df.rank(method=method, axis=axis)
    tm.assert_frame_equal(result, exp_df)
frame = df if dtype is None else df.astype(dtype)
_check2d(frame, self.results[method], method=method, axis=axis)
```

## Next Steps


---

*Source: test_rank.py:269 | Complexity: Advanced | Last updated: 2026-06-02*