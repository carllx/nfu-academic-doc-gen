# How To: Sum Deprecated Axis Behavior

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sum deprecated axis behavior

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.standard_normal(...)

```python
arr = np.random.default_rng(2).standard_normal((4, 3))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(arr)
```

### Step 3: Assign msg = 'The behavior of DataFrame.sum with axis=None is deprecated'

```python
msg = 'The behavior of DataFrame.sum with axis=None is deprecated'
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 5: Assign res = np.sum(...)

```python
res = np.sum(df)
```

### Step 6: Assign expected = df.sum(...)

```python
expected = df.sum(axis=None)
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).standard_normal((4, 3))
df = DataFrame(arr)
msg = 'The behavior of DataFrame.sum with axis=None is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg, check_stacklevel=False):
    res = np.sum(df)
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = df.sum(axis=None)
tm.assert_series_equal(res, expected)
```

## Next Steps


---

*Source: test_npfuncs.py:30 | Complexity: Intermediate | Last updated: 2026-06-02*