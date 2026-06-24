# How To: Group Diff Real Frame

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test group diff real frame

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_real_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3, 3, 2], 'b': [1, 2, 3, 4, 5], 'c': [1, 2, 3, 4, 6]}, dtype=any_real_numpy_dtype)
```

### Step 2: Assign result = df.groupby.diff(...)

```python
result = df.groupby('a').diff()
```

### Step 3: Assign exp_dtype = 'float'

```python
exp_dtype = 'float'
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': [np.nan, np.nan, np.nan, 1.0, 3.0], 'c': [np.nan, np.nan, np.nan, 1.0, 4.0]}, dtype=exp_dtype)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign exp_dtype = 'float32'

```python
exp_dtype = 'float32'
```


## Complete Example

```python
# Setup
# Fixtures: any_real_numpy_dtype

# Workflow
df = DataFrame({'a': [1, 2, 3, 3, 2], 'b': [1, 2, 3, 4, 5], 'c': [1, 2, 3, 4, 6]}, dtype=any_real_numpy_dtype)
result = df.groupby('a').diff()
exp_dtype = 'float'
if any_real_numpy_dtype in ['int8', 'int16', 'float32']:
    exp_dtype = 'float32'
expected = DataFrame({'b': [np.nan, np.nan, np.nan, 1.0, 3.0], 'c': [np.nan, np.nan, np.nan, 1.0, 4.0]}, dtype=exp_dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby_shift_diff.py:86 | Complexity: Intermediate | Last updated: 2026-06-02*